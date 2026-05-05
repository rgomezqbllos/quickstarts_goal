#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ui_runner.py
-------------
Pequeña interfaz web local para elegir una carpeta de Markdown y generar los
PDFs usando make_goalbus_pt_pdfs.run_pipeline (sin traducción).

Requisitos:
  pip install flask reportlab

Uso:
  python3 ui_runner.py
  (abre el navegador en http://127.0.0.1:5000)
"""

import threading
import webbrowser
from queue import Queue
from flask import Flask, request, jsonify, send_from_directory
import subprocess
import tempfile
import os
import sys
import shutil

from goalbus_pdf_pt import run_pipeline

PORT = 1234
app = Flask(__name__)
jobs = {}

_PS_FOLDER_FALLBACK = """\
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$shell = New-Object -ComObject Shell.Application
$folder = $shell.BrowseForFolder(0, "Selecciona carpeta de Markdown", 0x51)
if ($folder) { Write-Output $folder.Self.Path }
"""

_PS_FILE_PICKER = """\
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Add-Type -AssemblyName System.Windows.Forms
[void][System.Windows.Forms.Application]::EnableVisualStyles()
$owner = New-Object System.Windows.Forms.Form
$owner.TopMost = $true
$owner.StartPosition = "CenterScreen"
$owner.Size = New-Object System.Drawing.Size(0,0)
[void]$owner.Show()
[void]$owner.Focus()
$d = New-Object System.Windows.Forms.OpenFileDialog
$d.Filter = "PNG files (*.png)|*.png|All files (*.*)|*.*"
$d.Title = "Selecciona logo (png)"
if ($d.ShowDialog($owner) -eq "OK") { Write-Output $d.FileName }
$owner.Dispose()
"""


def _win_pick_folder_ctypes(title):
    """
    Llama a IFileOpenDialog directamente via ctypes de Python.
    - Sin PowerShell, sin Add-Type, sin dependencias externas.
    - Muestra el diálogo moderno del Explorador de Windows.
    - Devuelve siempre la ruta real del filesystem (rutas OneDrive incluidas).
    """
    try:
        import ctypes
        import ctypes.wintypes as wt

        class GUID(ctypes.Structure):
            _fields_ = [('Data1', wt.DWORD), ('Data2', wt.WORD),
                        ('Data3', wt.WORD), ('Data4', ctypes.c_ubyte * 8)]

        def make_guid(d1, d2, d3, *b):
            return GUID(d1, d2, d3, (ctypes.c_ubyte * 8)(*b))

        # CLSID_FileOpenDialog y IID_IFileOpenDialog
        CLSID = make_guid(0xDC1C5A9C, 0xE88A, 0x4DDE, 0xA5, 0xA1, 0x60, 0xF8, 0x2A, 0x20, 0xAE, 0xF7)
        IID   = make_guid(0xD57C7288, 0xD4AD, 0x4768, 0xBE, 0x02, 0x9D, 0x96, 0x95, 0x32, 0xD9, 0x60)

        ole32 = ctypes.windll.ole32
        ole32.CoInitialize(None)

        obj = ctypes.c_void_p()
        if ole32.CoCreateInstance(ctypes.byref(CLSID), None, 1,
                                  ctypes.byref(IID), ctypes.byref(obj)) != 0:
            return ""

        def vtfn(this, idx, *argtypes):
            """Devuelve el método del vtable COM en la posición idx."""
            tab = ctypes.cast(
                ctypes.cast(this, ctypes.POINTER(ctypes.c_void_p))[0],
                ctypes.POINTER(ctypes.c_void_p)
            )
            return ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_void_p, *argtypes)(tab[idx])

        # SetOptions: FOS_PICKFOLDERS(0x20) | FOS_FORCEFILESYSTEM(0x40)
        vtfn(obj, 9, wt.DWORD)(obj, 0x60)
        # SetTitle (vtable[17])
        vtfn(obj, 17, ctypes.c_wchar_p)(obj, title)
        # Show(hwnd=NULL) — vtable[3]; != 0 significa cancelado
        if vtfn(obj, 3, ctypes.c_void_p)(obj, None) != 0:
            return ""

        # GetResult → IShellItem* (vtable[20])
        item = ctypes.c_void_p()
        if vtfn(obj, 20, ctypes.POINTER(ctypes.c_void_p))(obj, ctypes.byref(item)) != 0:
            return ""

        # IShellItem::GetDisplayName(SIGDN_FILESYSPATH=0x80058000) → ruta real
        pbuf = ctypes.c_void_p()
        if vtfn(item, 5, wt.DWORD, ctypes.POINTER(ctypes.c_void_p))(
                item, 0x80058000, ctypes.byref(pbuf)) != 0 or not pbuf.value:
            return ""

        path = ctypes.wstring_at(pbuf.value)
        ole32.CoTaskMemFree(pbuf)
        return path
    except Exception:
        return ""


def _run_ps(script):
    """Escribe el script en un .ps1 temporal y lo ejecuta con UTF-8."""
    tmp = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.ps1',
                                         delete=False, encoding='utf-8') as f:
            f.write(script)
            tmp = f.name
        res = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", tmp],
            capture_output=True, encoding='utf-8', timeout=60
        )
        return res.stdout.strip() if res.returncode == 0 else ""
    except Exception:
        return ""
    finally:
        if tmp:
            try:
                os.unlink(tmp)
            except OSError:
                pass


def pick_folder():
    """
    Selector de carpeta multiplataforma sin Tk.
    - macOS: AppleScript.
    - Windows: IFileOpenDialog via COM (maneja OneDrive y rutas Unicode).
    - Linux: zenity (si está disponible).
    Devuelve '' si se cancela o no está disponible.
    """
    try:
        if sys.platform == "darwin":
            res = subprocess.run(
                ["osascript", "-e", 'POSIX path of (choose folder with prompt "Selecciona carpeta de Markdown")'],
                capture_output=True, text=True, timeout=60
            )
            if res.returncode == 0:
                return res.stdout.strip()
        elif os.name == "nt":
            path = _win_pick_folder_ctypes("Selecciona carpeta de Markdown")
            if not path:
                path = _run_ps(_PS_FOLDER_FALLBACK)
            return path
        else:
            if shutil.which("zenity"):
                res = subprocess.run(
                    ["zenity", "--file-selection", "--directory", "--title=Selecciona carpeta de Markdown"],
                    capture_output=True, text=True, timeout=60
                )
                if res.returncode == 0:
                    return res.stdout.strip()
    except Exception:
        return ""
    return ""


def pick_file():
    """
    Selector de archivo multiplataforma (para logo). Devuelve ruta o ''.
    """
    try:
        if sys.platform == "darwin":
            res = subprocess.run(
                ["osascript", "-e", 'POSIX path of (choose file with prompt "Selecciona logo (png)")'],
                capture_output=True, text=True, timeout=60
            )
            if res.returncode == 0:
                return res.stdout.strip()
        elif os.name == "nt":
            return _run_ps(_PS_FILE_PICKER)
        else:
            if shutil.which("zenity"):
                res = subprocess.run(
                    ["zenity", "--file-selection", "--title=Selecciona logo (png)", "--file-filter=*.png"],
                    capture_output=True, text=True, timeout=60
                )
                if res.returncode == 0:
                    return res.stdout.strip()
    except Exception:
        return ""
    return ""

@app.route("/")
def index():
    return send_from_directory(os.path.dirname(__file__), "ui_runner.html")

@app.route("/pick", methods=["POST"])
def pick():
    path = pick_folder()
    return jsonify({"path": path})

@app.route("/pick_logo", methods=["POST"])
def pick_logo():
    path = pick_file()
    return jsonify({"path": path})

@app.route("/ensure_out", methods=["POST"])
def ensure_out():
    data = request.get_json(force=True)
    md_dir = data.get("md_dir", "")
    out = data.get("out", "").strip()
    if not md_dir:
        return jsonify({"ok": False, "error": "Falta carpeta de Markdown"})
    target = out or os.path.join(md_dir, "result")
    try:
        os.makedirs(target, exist_ok=True)
        return jsonify({"ok": True, "path": target})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)})

def run_job(job_id, md_dir, logo, out, output_format, px_filter, lang):
    log_q = jobs[job_id]["log"]
    def log_fn(msg):
        log_q.put(msg)
    try:
        summary = run_pipeline(
            md_dir=md_dir,
            logo_path=logo,
            out_dir=out,
            output_format=output_format,
            px_filter=px_filter,
            log_fn=log_fn,
            lang=lang,
        )
        jobs[job_id]["summary"] = summary
    except Exception as e:
        log_q.put(f"ERROR: {e}")
    finally:
        log_q.put("__DONE__")

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json(force=True)
    md_dir = data.get("md_dir", "")
    logo = data.get("logo", "")
    out  = data.get("out", "")
    output_format = (data.get("output_format", "pdf") or "pdf").strip().lower()
    px_filter = data.get("px_filter", "")
    lang = data.get("lang", "auto")
    if output_format not in ("pdf", "docx"):
        return jsonify({"error": f"Formato no soportado: {output_format}"}), 400
    job_id = str(len(jobs) + 1)
    jobs[job_id] = {"log": Queue(), "summary": None}
    t = threading.Thread(target=run_job, args=(job_id, md_dir, logo, out, output_format, px_filter, lang), daemon=True)
    t.start()
    return jsonify({"job_id": job_id})

@app.route("/log/<job_id>")
def log(job_id):
    if job_id not in jobs:
        return jsonify({"lines": [], "done": True})
    q = jobs[job_id]["log"]
    lines = []
    while not q.empty():
        lines.append(q.get())
    done = "__DONE__" in lines
    lines = [l for l in lines if l != "__DONE__"]
    return jsonify({"lines": lines, "done": done, "summary": jobs[job_id].get("summary") if done else None})

def main():
    url = f"http://127.0.0.1:{PORT}"
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(host="127.0.0.1", port=PORT, debug=False)

if __name__ == "__main__":
    main()
