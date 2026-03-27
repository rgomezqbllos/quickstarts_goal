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
import os
import sys
import shutil

from goalbus_pdf_pt import run_pipeline

PORT = 1234
app = Flask(__name__)
jobs = {}

def pick_folder():
    """
    Selector de carpeta multiplataforma sin Tk.
    - macOS: AppleScript.
    - Windows: PowerShell + OpenFileDialog moderno (Explorador de Windows).
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
            cmd = (
                "Add-Type -AssemblyName System.Windows.Forms;"
                "[System.Windows.Forms.Application]::EnableVisualStyles();"
                "$owner = New-Object System.Windows.Forms.Form;"
                "$owner.TopMost = $true;"
                "$owner.StartPosition = 'CenterScreen';"
                "$owner.Size = New-Object System.Drawing.Size(0,0);"
                "$owner.Show();"
                "$owner.Focus();"
                "$d = New-Object System.Windows.Forms.OpenFileDialog;"
                "$d.ValidateNames = $false;"
                "$d.CheckFileExists = $false;"
                "$d.CheckPathExists = $true;"
                "$d.FileName = 'Selecciona esta carpeta.';"
                "$d.Title = 'Selecciona carpeta de Markdown';"
                "if ($d.ShowDialog($owner) -eq 'OK') {"
                "  [System.IO.Path]::GetDirectoryName($d.FileName)"
                "};"
                "$owner.Dispose()"
            )
            res = subprocess.run(
                ["powershell", "-NoProfile", "-Command", cmd],
                capture_output=True, text=True, timeout=60
            )
            if res.returncode == 0:
                return res.stdout.strip()
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
            cmd = (
                "Add-Type -AssemblyName System.Windows.Forms;"
                "[System.Windows.Forms.Application]::EnableVisualStyles();"
                "$owner = New-Object System.Windows.Forms.Form;"
                "$owner.TopMost = $true;"
                "$owner.StartPosition = 'CenterScreen';"
                "$owner.Size = New-Object System.Drawing.Size(0,0);"
                "$owner.Show();"
                "$owner.Focus();"
                "$d = New-Object System.Windows.Forms.OpenFileDialog;"
                "$d.Filter = 'PNG files (*.png)|*.png|All files (*.*)|*.*';"
                "$d.Title = 'Selecciona logo (png)';"
                "if ($d.ShowDialog($owner) -eq 'OK') { Write-Output $d.FileName };"
                "$owner.Dispose()"
            )
            res = subprocess.run(
                ["powershell", "-NoProfile", "-Command", cmd],
                capture_output=True, text=True, timeout=60
            )
            if res.returncode == 0:
                return res.stdout.strip()
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

def run_job(job_id, md_dir, logo, out, output_format):
    log_q = jobs[job_id]["log"]
    def log_fn(msg):
        log_q.put(msg)
    try:
        summary = run_pipeline(
            md_dir=md_dir,
            logo_path=logo,
            out_dir=out,
            output_format=output_format,
            log_fn=log_fn,
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
    if output_format not in ("pdf", "docx"):
        return jsonify({"error": f"Formato no soportado: {output_format}"}), 400
    job_id = str(len(jobs) + 1)
    jobs[job_id] = {"log": Queue(), "summary": None}
    t = threading.Thread(target=run_job, args=(job_id, md_dir, logo, out, output_format), daemon=True)
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
