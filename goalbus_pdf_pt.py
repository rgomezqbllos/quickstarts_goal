#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
goalbus_pdf_pt.py
─────────────────
Convierte archivos Markdown de goalbus (ya en PORTUGUÉS) a PDFs imprimibles.

REQUISITO (instalar una sola vez):
    pip install reportlab

USO — carpeta completa:
    python3 goalbus_pdf_pt.py --md-dir "/ruta/a/markdowns_pt/"

USO — archivo individual:
    python3 goalbus_pdf_pt.py --md "/ruta/a/P10_foo.md"

OPCIONES:
    --md-dir   Carpeta con archivos Pxx_*.md en portugués
    --md       Archivo markdown individual
    --logo     Ruta a goal-logo-white.png (opcional; se busca automáticamente)
    --out      Carpeta de salida (por defecto: misma que --md-dir o --md)
    --from N   Procesar desde el número N (por defecto: 1)
    --to   N   Procesar hasta el número N (por defecto: 99)

SALIDA:
    P01_QuickStart_Imprimivel.pdf, P02_..., etc.
"""

import sys, os, re, argparse

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor
    from reportlab.lib.utils import ImageReader
    from reportlab.platypus import SimpleDocTemplate, Spacer, KeepTogether
    from reportlab.platypus.flowables import Flowable
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
except ImportError:
    print("ERROR: Falta 'reportlab'. Instala con:  pip install reportlab")
    sys.exit(1)

# ── Colores ─────────────────────────────────────────────────────────────────
BG_PAGE    = HexColor("#0D1520"); BG_CARD    = HexColor("#141F30")
BG_CARD_ALT= HexColor("#1A2640"); BG_SURFACE = HexColor("#0A1018")
TEAL       = HexColor("#6EF8EC"); TEAL_DIM   = HexColor("#2BC4BA")
BLUE_LIGHT = HexColor("#60A5FA"); TEXT_WHITE = HexColor("#F0F4F8")
TEXT_GRAY  = HexColor("#94A3B8"); TEXT_DIM   = HexColor("#64748B")
WARN       = HexColor("#FBBF24"); SUCCESS    = HexColor("#34D399")
W, H = letter; PAD = 0.45 * inch
TOP_MARGIN = 0.75 * inch
BOTTOM_MARGIN = 0.6 * inch
CONTENT_MAX_IMAGE_FRAC = 0.70
_LOGO_RATIO = 1868 / 1031
LOGO_PATH = ""  # se asigna en main()
ALLOWED_IMAGE_EXTS = (".png", ".jpg", ".jpeg")
REF_LINE_RE = re.compile(r'^\s*ref:\s*(.*?)\s*$', re.IGNORECASE)

# ── Fuentes (detección automática: macOS / Linux / Windows) ─────────────────
def _setup_fonts():
    def try_reg(name, paths):
        for p in paths:
            if os.path.exists(p):
                try:
                    pdfmetrics.registerFont(TTFont(name, p))
                    return True
                except Exception:
                    pass
        return False

    regular = [
        "/System/Library/Fonts/Supplemental/Arial.ttf",  # macOS Catalina+
        "/Library/Fonts/Arial.ttf",
        os.path.expanduser("~/Library/Fonts/Arial.ttf"),
        "/System/Library/Fonts/Supplemental/Verdana.ttf",
        "/Library/Fonts/Verdana.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",      # Linux
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "C:/Windows/Fonts/arial.ttf",                           # Windows
        "C:/Windows/Fonts/segoeui.ttf",
    ]
    bold = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        os.path.expanduser("~/Library/Fonts/Arial Bold.ttf"),
        "/System/Library/Fonts/Supplemental/Verdana Bold.ttf",
        "/Library/Fonts/Verdana Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/segoeuib.ttf",
    ]

    ok_r = try_reg("Inter", regular)
    ok_b = try_reg("Inter-Bold", bold)

    # Último recurso: escanear carpetas del sistema
    if not ok_r or not ok_b:
        for d in ["/System/Library/Fonts/Supplemental/", "/Library/Fonts/",
                  os.path.expanduser("~/Library/Fonts/"), "/usr/share/fonts/"]:
            if not os.path.isdir(d): continue
            for f in sorted(os.listdir(d)):
                if not f.lower().endswith(".ttf"): continue
                p = os.path.join(d, f)
                if not ok_r:
                    try: pdfmetrics.registerFont(TTFont("Inter", p)); ok_r = True
                    except Exception: pass
                if not ok_b and ok_r:
                    try: pdfmetrics.registerFont(TTFont("Inter-Bold", p)); ok_b = True
                    except Exception: pass
                if ok_r and ok_b: break
            if ok_r and ok_b: break

_setup_fonts()

# ── Utilidades de texto ──────────────────────────────────────────────────────
def parse_bold(text):
    parts, i, r = text.split("**"), 0, []
    for p in parts: r.append((p, i % 2 == 1)); i += 1
    return r

def measure_wrapped_bold(text, size, max_w):
    from reportlab.pdfbase.pdfmetrics import stringWidth
    words = [(w, b) for seg, b in parse_bold(text) for w in seg.split()]
    lh = size * 1.45; lines = 1; cur_w = 0
    for w, b in words:
        f = "Inter-Bold" if b else "Inter"
        ww = stringWidth(w, f, size); sp = stringWidth(" ", "Inter", size)
        if cur_w == 0: cur_w = ww
        elif cur_w + sp + ww <= max_w: cur_w += sp + ww
        else: lines += 1; cur_w = ww
    return lines * lh

def draw_wrapped_bold(c, text, x, start_y, size, max_w, cn, cb):
    words = [(w, b) for seg, b in parse_bold(text) for w in seg.split()]
    lh = size * 1.45; y = start_y; cur = []
    def lw(ws): return sum(c.stringWidth(w, "Inter-Bold" if b else "Inter", size) + (c.stringWidth(" ", "Inter", size) if i < len(ws)-1 else 0) for i, (w, b) in enumerate(ws))
    def flush(ws, yy):
        cx = x
        for w, b in ws:
            f = "Inter-Bold" if b else "Inter"; c.setFillColor(cb if b else cn)
            c.setFont(f, size); c.drawString(cx, yy, w)
            cx += c.stringWidth(w, f, size) + c.stringWidth(" ", "Inter", size)
    for word, bold in words:
        test = cur + [(word, bold)]
        if lw(test) <= max_w: cur = test
        else:
            if cur: flush(cur, y); y -= lh
            cur = [(word, bold)]
    if cur: flush(cur, y); y -= lh
    return y

# ── Header / Footer ──────────────────────────────────────────────────────────
def make_bg(label, footer):
    top_pad = 8  # ~2.8 mm of aire sobre el logo
    def _bg(c, doc):
        c.saveState()
        c.setFillColor(BG_PAGE); c.rect(0, 0, W, H, fill=1, stroke=0)
        header_y = H-0.55*inch - top_pad
        c.setFillColor(BG_SURFACE); c.rect(0, header_y, W, 0.55*inch, fill=1, stroke=0)
        if LOGO_PATH and os.path.exists(LOGO_PATH):
            lw, lh2 = 1.1*inch, 1.1*inch/_LOGO_RATIO
            c.drawImage(LOGO_PATH, PAD, header_y+(0.55*inch-lh2)/2, width=lw, height=lh2, mask="auto")
        c.setFont("Inter", 7.5); c.setFillColor(TEXT_DIM)
        c.drawRightString(W-PAD, header_y+0.18*inch, label)
        c.setFillColor(BG_SURFACE); c.rect(0, 0, W, 0.38*inch, fill=1, stroke=0)
        c.setFont("Inter", 7); c.setFillColor(TEXT_DIM)
        c.drawString(PAD, 0.13*inch, footer)
        c.drawRightString(W-PAD, 0.13*inch, f"Página {doc.page}")
        c.restoreState()
    return _bg

# ── Flowables ────────────────────────────────────────────────────────────────
class HeroBlock(Flowable):
    def __init__(self, number, title, intro):
        super().__init__(); self.number = number; self.title = title; self.intro = intro; self.avail = W-2*PAD
    def _h(self):
        return 0.32*inch + measure_wrapped_bold(self.title, 18, self.avail-0.8*inch) + 0.12*inch + measure_wrapped_bold(self.intro, 9.5, self.avail-0.1*inch) + 0.28*inch
    def wrap(self, aw, ah): self.width = aw; self.height = self._h(); return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_CARD); c.roundRect(0, 0, aw, self.height, 8, fill=1, stroke=0)
        c.setFillColor(TEAL_DIM); c.rect(0, 0, 4, self.height, fill=1, stroke=0)
        y = self.height-0.32*inch; c.setFont("Inter-Bold", 11); c.setFillColor(TEAL); c.drawString(0.18*inch, y, f"P{self.number}")
        y = draw_wrapped_bold(c, self.title, 0.18*inch, y-0.02*inch-18*1.2, 18, aw-0.8*inch, TEXT_WHITE, TEAL) - 0.06*inch
        draw_wrapped_bold(c, self.intro, 0.18*inch, y, 9.5, aw-0.3*inch, TEXT_GRAY, TEXT_WHITE)

class SectionHeader(Flowable):
    def __init__(self, text, number=None):
        super().__init__(); self.text = text; self.number = number; self.avail = W-2*PAD
    def wrap(self, aw, ah):
        self.width = aw
        max_w = self.avail-0.65*inch if self.number else self.avail-0.3*inch
        self.height = measure_wrapped_bold(self.text, 12.5, max_w) + 0.32*inch
        return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_CARD_ALT); c.roundRect(0, 0, aw, self.height, 6, fill=1, stroke=0)
        c.setFillColor(TEAL); c.rect(0, 0, 3, self.height, fill=1, stroke=0)
        max_w = self.avail-0.65*inch if self.number else self.avail-0.3*inch
        text_h = measure_wrapped_bold(self.text, 12.5, max_w)
        text_y = (self.height + text_h)/2 - 12.5*0.25
        if self.number:
            c.setFont("Inter-Bold", 9); c.setFillColor(TEAL_DIM)
            num_y = (self.height - 9)/2
            c.drawString(0.18*inch, num_y, f"0{self.number}" if self.number < 10 else str(self.number))
            draw_wrapped_bold(c, self.text, 0.52*inch, text_y, 12.5, max_w, TEXT_WHITE, TEAL)
        else:
            draw_wrapped_bold(c, self.text, 0.18*inch, text_y, 12.5, max_w, TEXT_WHITE, TEAL)

class BodyText(Flowable):
    def __init__(self, text, size=9.5, color=None):
        super().__init__(); self.text = text; self.size = size; self.color = color or TEXT_GRAY; self.avail = W-2*PAD
    def wrap(self, aw, ah): self.width = aw; self.height = measure_wrapped_bold(self.text, self.size, self.avail); return aw, self.height
    def draw(self): draw_wrapped_bold(self.canv, self.text, 0, self.height-self.size*0.25, self.size, self.avail, self.color, TEXT_WHITE)

class PrereqBox(Flowable):
    def __init__(self, items):
        super().__init__(); self.items = items; self.avail = W-2*PAD
    def _h(self):
        h = 0.28*inch
        for it in self.items: h += measure_wrapped_bold("•  "+it, 9, self.avail-0.55*inch) + 4
        return h + 0.18*inch
    def wrap(self, aw, ah): self.width = aw; self.height = self._h(); return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_SURFACE); c.roundRect(0, 0, aw, self.height, 6, fill=1, stroke=0)
        c.setStrokeColor(WARN); c.setLineWidth(1); c.roundRect(0, 0, aw, self.height, 6, fill=0, stroke=1)
        y = self.height-0.2*inch
        for it in self.items:
            ih = measure_wrapped_bold("•  "+it, 9, aw-0.55*inch); y -= ih
            draw_wrapped_bold(c, "•  "+it, 0.22*inch, y+ih-9*0.25, 9, aw-0.55*inch, TEXT_GRAY, TEXT_WHITE); y -= 4

class CaseRefBox(Flowable):
    def __init__(self, text):
        super().__init__(); self.text = text; self.avail = W-2*PAD
    def wrap(self, aw, ah):
        self.width = aw; self.height = measure_wrapped_bold(self.text, 9.5, self.avail-0.65*inch) + 0.52*inch; return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_CARD); c.roundRect(0, 0, aw, self.height, 6, fill=1, stroke=0)
        c.setStrokeColor(BLUE_LIGHT); c.setLineWidth(1); c.roundRect(0, 0, aw, self.height, 6, fill=0, stroke=1)
        draw_wrapped_bold(c, self.text, 0.18*inch, self.height-0.2*inch, 9.5, aw-0.38*inch, TEXT_GRAY, TEXT_WHITE)

class NumberedStepsList(Flowable):
    def __init__(self, steps):
        super().__init__(); self.steps = steps; self.avail = W-2*PAD
    def _h(self):
        h = 0.22*inch; ind = PAD+26
        for s in self.steps:
            mw = self.avail-0.45*inch if s.get("snum", "") == "•" else self.avail-(ind-PAD)-0.22*inch
            h += measure_wrapped_bold(s["text"], 9, mw) + 5
            for sub in s.get("subs", []):
                sub_text = sub.get("text") if isinstance(sub, dict) else str(sub)
                h += measure_wrapped_bold(sub_text, 8.5, self.avail-0.85*inch) + 4
        return h + 0.12*inch
    def wrap(self, aw, ah): self.width = aw; self.height = self._h(); return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_CARD); c.roundRect(0, 0, aw, self.height, 6, fill=1, stroke=0)
        ind = 0.36*inch; y = self.height-0.28*inch
        for s in self.steps:
            snum = s.get("snum", ""); is_b = (snum == "•")
            tx = ind+0.22*inch if not is_b else 0.35*inch
            mw = aw-tx-0.1*inch; th = measure_wrapped_bold(s["text"], 9, mw); y -= th
            fy = y+th-9*0.25
            if is_b:
                c.setFillColor(TEAL); c.setFont("Inter-Bold", 11); c.drawString(0.18*inch, fy, "•")
            else:
                bw = c.stringWidth(str(snum), "Inter-Bold", 8.5); cy = fy+9*0.35
                c.setFillColor(TEAL_DIM); c.circle(ind, cy, 8, fill=1, stroke=0)
                c.setFont("Inter-Bold", 8); c.setFillColor(BG_PAGE); c.drawString(ind-bw/2, cy-3.5, str(snum))
            draw_wrapped_bold(c, s["text"], tx, fy, 9, mw, TEXT_GRAY, TEXT_WHITE); y -= 5
            for sub in s.get("subs", []):
                if isinstance(sub, dict):
                    sub_text = sub.get("text", "")
                    sub_snum = sub.get("snum", "–")
                else:
                    sub_text = str(sub); sub_snum = "–"
                sh = measure_wrapped_bold(sub_text, 8.5, aw-0.75*inch); y -= sh; fy2 = y+sh-8.5*0.25
                c.setFont("Inter", 8.5); c.setFillColor(TEXT_DIM)
                if isinstance(sub_snum, int):
                    c.drawString(0.55*inch, fy2, f"{sub_snum}.")
                elif sub_snum == "•":
                    c.setFont("Inter-Bold", 9); c.setFillColor(TEAL_DIM)
                    c.drawString(0.55*inch, fy2, "•")
                    c.setFont("Inter", 8.5); c.setFillColor(TEXT_DIM)
                else:
                    c.drawString(0.55*inch, fy2, "–")
                draw_wrapped_bold(c, sub_text, 0.68*inch, fy2, 8.5, aw-0.78*inch, TEXT_DIM, TEXT_GRAY); y -= 4

class ExampleBox(Flowable):
    def __init__(self, title, items, numbered=True):
        super().__init__(); self.title = title; self.items = items; self.numbered = numbered; self.avail = W-2*PAD
    def _h(self):
        h = 0.32*inch
        for it in self.items: h += measure_wrapped_bold(it, 9, self.avail-0.55*inch) + 5
        return h + 0.12*inch
    def wrap(self, aw, ah): self.width = aw; self.height = self._h(); return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_CARD_ALT); c.roundRect(0, 0, aw, self.height, 6, fill=1, stroke=0)
        c.setStrokeColor(SUCCESS); c.setLineWidth(0.8); c.roundRect(0, 0, aw, self.height, 6, fill=0, stroke=1)
        if self.title:
            c.setFont("Inter-Bold", 8); c.setFillColor(SUCCESS); c.drawString(0.18*inch, self.height-0.21*inch, self.title)
            y = self.height-0.36*inch
        else:
            y = self.height-0.2*inch
        for i, it in enumerate(self.items):
            ih = measure_wrapped_bold(it, 9, aw-0.55*inch); y -= ih; fy = y+ih-9*0.25
            if self.numbered:
                c.setFont("Inter-Bold", 8.5); c.setFillColor(SUCCESS); c.drawString(0.18*inch, fy, f"{i+1}.")
                draw_wrapped_bold(c, it, 0.38*inch, fy, 9, aw-0.52*inch, TEXT_GRAY, TEXT_WHITE)
            else:
                c.setFont("Inter-Bold", 11); c.setFillColor(SUCCESS); c.drawString(0.18*inch, fy, "•")
                draw_wrapped_bold(c, it, 0.35*inch, fy, 9, aw-0.5*inch, TEXT_GRAY, TEXT_WHITE)
            y -= 5

class QuestionList(Flowable):
    def __init__(self, title, items):
        super().__init__(); self.title = title; self.items = items; self.avail = W-2*PAD
    def _h(self):
        h = 0.32*inch
        for it in self.items: h += measure_wrapped_bold(it, 9, self.avail-0.55*inch) + 5
        return h + 0.12*inch
    def wrap(self, aw, ah): self.width = aw; self.height = self._h(); return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_SURFACE); c.roundRect(0, 0, aw, self.height, 6, fill=1, stroke=0)
        c.setStrokeColor(TEAL_DIM); c.setLineWidth(0.8); c.roundRect(0, 0, aw, self.height, 6, fill=0, stroke=1)
        if self.title:
            c.setFont("Inter-Bold", 8); c.setFillColor(TEAL); c.drawString(0.18*inch, self.height-0.21*inch, self.title)
            y = self.height-0.36*inch
        else:
            y = self.height-0.2*inch
        for it in self.items:
            ih = measure_wrapped_bold(it, 9, aw-0.55*inch); y -= ih; fy = y+ih-9*0.25
            c.setFont("Inter-Bold", 9); c.setFillColor(TEAL_DIM); c.drawString(0.18*inch, fy, "✓")
            draw_wrapped_bold(c, it, 0.36*inch, fy, 9, aw-0.52*inch, TEXT_GRAY, TEXT_WHITE); y -= 5

class ClosingNote(Flowable):
    def __init__(self, text):
        super().__init__(); self.text = text; self.avail = W-2*PAD
    def wrap(self, aw, ah):
        self.width = aw; self.height = measure_wrapped_bold(self.text, 9, self.avail-0.5*inch) + 0.38*inch; return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_CARD_ALT); c.roundRect(0, 0, aw, self.height, 6, fill=1, stroke=0)
        c.setFillColor(SUCCESS); c.rect(0, 0, 3, self.height, fill=1, stroke=0)
        draw_wrapped_bold(c, self.text, 0.18*inch, self.height-0.22*inch, 9, aw-0.3*inch, TEXT_GRAY, TEXT_WHITE)

class FurtherReadingBox(Flowable):
    def __init__(self, items):
        super().__init__(); self.items = items; self.avail = W-2*PAD
    def _h(self):
        h = 0.32*inch
        for it in self.items: h += measure_wrapped_bold(it, 9, self.avail-0.55*inch) + 5
        return h + 0.12*inch
    def wrap(self, aw, ah): self.width = aw; self.height = self._h(); return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_CARD); c.roundRect(0, 0, aw, self.height, 6, fill=1, stroke=0)
        c.setStrokeColor(BLUE_LIGHT); c.setLineWidth(0.8); c.roundRect(0, 0, aw, self.height, 6, fill=0, stroke=1)
        y = self.height-0.2*inch
        for it in self.items:
            ih = measure_wrapped_bold(it, 9, aw-0.55*inch); y -= ih; fy = y+ih-9*0.25
            c.setFont("Inter", 9); c.setFillColor(BLUE_LIGHT); c.drawString(0.18*inch, fy, "→")
            draw_wrapped_bold(c, it, 0.34*inch, fy, 9, aw-0.48*inch, BLUE_LIGHT, TEXT_WHITE); y -= 5

class RefWarningBox(Flowable):
    def __init__(self, text):
        super().__init__(); self.text = text; self.avail = W-2*PAD
    def wrap(self, aw, ah):
        self.width = aw
        self.height = measure_wrapped_bold(self.text, 8.7, self.avail-0.36*inch) + 0.35*inch
        return aw, self.height
    def draw(self):
        c = self.canv; aw = self.avail
        c.setFillColor(BG_SURFACE); c.roundRect(0, 0, aw, self.height, 5, fill=1, stroke=0)
        c.setStrokeColor(WARN); c.setLineWidth(0.8); c.roundRect(0, 0, aw, self.height, 5, fill=0, stroke=1)
        draw_wrapped_bold(c, self.text, 0.18*inch, self.height-0.21*inch, 8.7, aw-0.3*inch, WARN, TEXT_WHITE)

class ImageRefBlock(Flowable):
    def __init__(self, image_path, max_height):
        super().__init__()
        self.image_path = image_path
        self.max_height = max_height
        self._image_reader = None
        self._draw_w = 1.0
        self._draw_h = 1.0
        self._vpad = 0.08 * inch

    def _compute_size(self, avail_w):
        if self._image_reader is None:
            self._image_reader = ImageReader(self.image_path)
        img_w, img_h = self._image_reader.getSize()
        max_w = max(1.0, avail_w)
        max_h = max(1.0, self.max_height)
        scale = min(1.0, max_w / float(img_w), max_h / float(img_h))
        self._draw_w = max(1.0, img_w * scale)
        self._draw_h = max(1.0, img_h * scale)

    def wrap(self, aw, ah):
        self.width = aw
        self._compute_size(aw)
        self.height = self._draw_h + (2 * self._vpad)
        return aw, self.height

    def split(self, aw, ah):
        return []

    def draw(self):
        x = max(0.0, (self.width - self._draw_w) / 2.0)
        self.canv.drawImage(
            self.image_path,
            x,
            self._vpad,
            width=self._draw_w,
            height=self._draw_h,
            mask="auto",
        )

SP = lambda n=1: Spacer(1, n*0.13*inch)

# ── Parser de Markdown (patrones en PORTUGUÉS) ───────────────────────────────
_IMPERATIVE = [
    'abra ', 'faça ', 'revise ', 'selecione ', 'verifique ', 'confirme ',
    'salve ', 'guarde ', 'execute ', 'lance ', 'localize ', 'insira ',
    'atribua ', 'adicione ', 'aguarde ', 'volte ', 'decida ', 'identifique ',
    'detecte ', 'relacione ', 'evite ', 'documente ', 'conserve ', 'mantenha ',
    'duplique ', 'crie ', 'marque ', 'repita ', 'defina ', 'use ', 'ajuste ',
    'retome ', 'atualize ', 'filtre ', 'acesse ', 'navegue ', 'clique ',
    'carregue ', 'baixe ', 'importe ', 'exporte ', 'pressione ', 'configure ',
    'no goalbus', 'dentro do', 'dentro da', 'se o ', 'se a ', 'se não ', 'se exist',
    'na barra', 'no módulo', 'na tela', 'em goalbus', 'na seção',
    'abra o ', 'abra a ', 'vá para', 'vá ao ', 'vá à ',
]

def _is_instruction(items):
    if not items: return False
    first = items[0].get('text', '').lower().strip()
    return any(first.startswith(v) for v in _IMPERATIVE)

def _classify(items, ctx, is_bullet=False):
    c = ctx.lower()
    if any(k in c for k in ['antes de começar', 'antes de continuar', 'antes de prosseguir',
                              'antes de terminar', 'certifique-se de que', 'verifique se você']):
        return 'prereq'
    if 'para o caso de referência' in c or 'para o seu caso de referência' in c:
        is_q = any(k in c for k in ['confirme', 'certifique-se', 'afirmar', 'não continue',
                                     'não prossiga', 'não considere', 'termine este quick',
                                     'apenas quando puder', 'pergunte-se', 'pergunte se'])
        if is_q or (items and items[0].get('text', '').startswith('?')):
            return 'question'
        return 'example_bullet' if is_bullet else 'example_num'
    if is_bullet:
        return 'further'
    if _is_instruction(items):
        return 'steps'
    return 'inline'

def _parse_list(lines, i):
    items = []
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^(\d+)\.\s+(.*)', line)
        if m: items.append({'snum': int(m.group(1)), 'text': m.group(2).strip()}); i += 1; continue
        m = re.match(r'^-\s+(.*)', line)
        if m: items.append({'snum': '•', 'text': m.group(1).strip()}); i += 1; continue
        m = re.match(r'^\s{2,}(\d+)\.\s+(.*)', line)
        if m:
            if items:
                items[-1].setdefault('subs', []).append({'snum': int(m.group(1)), 'text': m.group(2).strip()})
            i += 1; continue
        m = re.match(r'^\s{2,}-\s+(.*)', line)
        if m:
            if items:
                items[-1].setdefault('subs', []).append({'snum': '•', 'text': m.group(1).strip()})
            i += 1; continue
        if not line.strip():
            j = i+1
            while j < len(lines) and not lines[j].strip(): j += 1
            if j < len(lines) and (re.match(r'^\d+\.', lines[j]) or re.match(r'^-\s', lines[j]) or re.match(r'^\s{2,}', lines[j])):
                i = j; continue
            else: break
        break
    return items, i

def extract_ref_name(line):
    m = REF_LINE_RE.match(line or "")
    if not m:
        return None
    return m.group(1).strip()

def _guide_dir_candidates(md_dir, p_num):
    dirs = [os.path.join(md_dir, f"P{p_num}")]
    p_padded = f"P{p_num:02d}"
    if p_padded != f"P{p_num}":
        dirs.append(os.path.join(md_dir, p_padded))
    return dirs

def _candidate_ref_names(ref_raw):
    name = (ref_raw or "").strip().strip("'\"")
    if not name or "/" in name or "\\" in name:
        return []
    base, ext = os.path.splitext(name)
    if ext:
        if ext.lower() in ALLOWED_IMAGE_EXTS:
            return [name]
        # Soporta nombres sin extension que incluyen puntos (ej. "...11.27.55").
        if ext[1:].isalpha() and len(ext) <= 5:
            return []
        return [f"{name}{extn}" for extn in ALLOWED_IMAGE_EXTS]
    return [f"{base}{extn}" for extn in ALLOWED_IMAGE_EXTS]

def _find_file_case_insensitive(folder, file_name):
    if not os.path.isdir(folder):
        return None
    target = file_name.lower()
    for item in os.listdir(folder):
        if item.lower() == target:
            path = os.path.join(folder, item)
            if os.path.isfile(path):
                return path
    return None

def resolve_ref_image(md_dir, p_num, ref_raw):
    names = _candidate_ref_names(ref_raw)
    if not names:
        return None
    for folder in _guide_dir_candidates(md_dir, p_num):
        for name in names:
            candidate = os.path.join(folder, name)
            if os.path.isfile(candidate):
                return candidate
            candidate_ci = _find_file_case_insensitive(folder, name)
            if candidate_ci:
                return candidate_ci
    return None

def _validate_image_refs(blocks, md_dir, p_num, ref_cache, log_fn):
    searched_dirs = [os.path.basename(d) for d in _guide_dir_candidates(md_dir, p_num)]
    for block in blocks:
        if block[0] == 'image_ref_invalid':
            log_fn(f"    [ref] AVISO P{p_num}: referencia invalida ({block[1] or 'ref:'})")
            continue
        if block[0] != 'image_ref':
            continue
        ref_raw = block[1]
        key = (p_num, ref_raw)
        if key in ref_cache:
            continue
        image_path = resolve_ref_image(md_dir, p_num, ref_raw)
        ref_cache[key] = image_path
        if image_path:
            rel = os.path.relpath(image_path, md_dir)
            log_fn(f"    [ref] OK P{p_num}: '{ref_raw}' -> {rel}")
        else:
            log_fn(f"    [ref] AVISO P{p_num}: no se encontro '{ref_raw}' en {', '.join(searched_dirs)}")

def _parse_section_body(body):
    lines = body.split('\n')
    blocks = []
    pending = []

    def flush():
        if pending:
            t = ' '.join(pending).strip()
            if t:
                if any(k in t.lower() for k in ['quando terminar', 'quando concluir',
                                                  'ao terminar', 'ao concluir']):
                    blocks.append(('closing', t))
                else:
                    blocks.append(('body', t))
            pending.clear()

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip(): flush(); i += 1; continue
        ref_name = extract_ref_name(line)
        if ref_name is not None:
            flush()
            if ref_name:
                blocks.append(('image_ref', ref_name))
            else:
                blocks.append(('image_ref_invalid', line.strip()))
            i += 1
            continue
        if line.startswith('>'):
            flush()
            bq = []
            while i < len(lines) and lines[i].startswith('>'):
                bq.append(lines[i].lstrip('> ').strip()); i += 1
            text = ' '.join(bq)
            blocks.append(('case_ref', text)); continue
        if re.match(r'^\d+\.\s', line):
            ctx = ' '.join(pending); flush()
            items, i = _parse_list(lines, i)
            kind = _classify(items, ctx, False)
            if kind == 'prereq':
                blocks.append(('prereq', [it['text'] for it in items]))
            elif kind == 'steps':
                blocks.append(('steps', items))
            elif kind == 'question':
                blocks.append(('question', '', [it['text'] for it in items]))
            elif kind == 'example_num':
                blocks.append(('example', '', [it['text'] for it in items], True))
            else:
                blocks.append(('steps', items))
            continue
        if re.match(r'^-\s', line):
            ctx = ' '.join(pending); flush()
            items, i = _parse_list(lines, i)
            kind = _classify(items, ctx, True)
            link_items = []
            for it in items:
                t = it['text']
                lm = re.match(r'\[([^\]]+)\]\([^\)]+\)', t)
                link_items.append(lm.group(1) if lm else t)
            if kind == 'further':
                blocks.append(('further', link_items))
            elif kind in ('example_bullet', 'example_num'):
                blocks.append(('example', '', link_items, False))
            elif kind == 'question':
                blocks.append(('question', '', link_items))
            else:
                blocks.append(('steps', items))
            continue
        pending.append(line.strip()); i += 1

    flush()
    return blocks

def _blocks_to_flowables(blocks, sec_title, sec_num, is_further, md_dir, p_num, ref_cache, image_max_h):
    fl = [KeepTogether([SectionHeader(sec_title, sec_num if not is_further else None), SP()])]
    for b in blocks:
        kind = b[0]
        if kind == 'body':       fl += [BodyText(b[1]), SP()]
        elif kind == 'closing':  fl += [ClosingNote(b[1]), SP(2)]
        elif kind == 'case_ref': fl += [CaseRefBox(b[1]), SP()]
        elif kind == 'prereq':   fl += [PrereqBox(b[1]), SP()]
        elif kind == 'steps':    fl += [NumberedStepsList(b[1]), SP()]
        elif kind == 'question': fl += [QuestionList(b[1].strip().rstrip(':'), b[2]), SP()]
        elif kind == 'example':  fl += [ExampleBox(b[1].strip().rstrip(':'), b[2], numbered=b[3]), SP()]
        elif kind == 'further':  fl += [FurtherReadingBox(b[1]), SP()]
        elif kind == 'image_ref':
            image_path = ref_cache.get((p_num, b[1]))
            if image_path:
                fl += [KeepTogether([ImageRefBlock(image_path, image_max_h), SP()])]
            else:
                fl += [RefWarningBox(f"Imagen no encontrada para referencia: ref: {b[1]}"), SP()]
        elif kind == 'image_ref_invalid':
            fl += [RefWarningBox("Referencia de imagen vacia o invalida. Usa: ref: nombre_imagen"), SP()]
    return fl

# ── Builder principal ────────────────────────────────────────────────────────
def build_pdf(md_path, out_dir, log_fn=print):
    basename = os.path.basename(md_path)
    base_no_ext = os.path.splitext(basename)[0]
    m = re.match(r'^P(\d+)', basename, re.IGNORECASE)
    p_num = int(m.group(1)) if m else 0
    md_dir = os.path.dirname(os.path.abspath(md_path))

    with open(md_path, 'r', encoding='utf-8') as f:
        raw = f.read()
    raw = re.sub(r'\s*filecite\S*', '', raw)

    meta = {}
    fm = re.match(r'^---\s*\n(.*?)\n---\s*\n', raw, re.DOTALL)
    if fm:
        for line in fm.group(1).split('\n'):
            mm = re.match(r'^(\w+):\s*(.*)', line)
            if mm: meta[mm.group(1)] = mm.group(2).strip().strip("'\"")
        raw = raw[fm.end():]
    title = meta.get('title', f'Quick Start P{p_num}')
    intro = meta.get('intro', '')

    parts = re.split(r'\n## ', '\n'+raw)
    sections = [(p.split('\n', 1)[0].strip(), p.split('\n', 1)[1] if '\n' in p else '') for p in parts[1:]]

    bg = make_bg(f"goalbus  •  Quick Start P{p_num}", f"goalbus  •  {title[:60]}")
    story = [HeroBlock(p_num, title, intro), SP(2)]
    image_max_h = (H - TOP_MARGIN - BOTTOM_MARGIN) * CONTENT_MAX_IMAGE_FRAC

    parsed_sections = []
    sec_num = 0
    for sec_title, sec_body in sections:
        is_further = any(k in sec_title.lower() for k in ['leituras adicionais', 'lecturas adicionales'])
        if not is_further:
            sec_num += 1
        blocks = _parse_section_body(sec_body)
        parsed_sections.append((sec_title, sec_num if not is_further else None, is_further, blocks))

    ref_cache = {}
    for _, _, _, blocks in parsed_sections:
        _validate_image_refs(blocks, md_dir, p_num, ref_cache, log_fn)

    for sec_title, sec_index, is_further, blocks in parsed_sections:
        story.extend(_blocks_to_flowables(
            blocks,
            sec_title,
            sec_index,
            is_further,
            md_dir,
            p_num,
            ref_cache,
            image_max_h,
        ))

    out_path = os.path.join(out_dir, f"{base_no_ext}.pdf")
    doc = SimpleDocTemplate(out_path, pagesize=letter,
                            leftMargin=PAD, rightMargin=PAD,
                            topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN)
    doc.build(story, onFirstPage=bg, onLaterPages=bg)
    return out_path

# ── Entry point ──────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='goalbus Quick Start PDF generator (PT)')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--md-dir', help='Carpeta con archivos Pxx_*.md en portugués')
    group.add_argument('--md',     help='Archivo markdown individual')
    parser.add_argument('--logo',  default='', help='Ruta a goal-logo-white.png')
    parser.add_argument('--out',   default='', help='Carpeta de salida')
    parser.add_argument('--from',  dest='p_from', type=int, default=1)
    parser.add_argument('--to',    dest='p_to',   type=int, default=99)
    args = parser.parse_args()

    global LOGO_PATH

    if args.md:
        # Archivo individual
        md_dir  = os.path.dirname(os.path.abspath(args.md))
        out_dir = args.out or md_dir
        md_files = []
        m = re.match(r'^P(\d+)', os.path.basename(args.md), re.IGNORECASE)
        if m: md_files = [(int(m.group(1)), args.md)]
    else:
        md_dir  = args.md_dir.rstrip('/')
        out_dir = args.out or md_dir
        md_files = []
        for fname in sorted(os.listdir(md_dir)):
            m = re.match(r'^P(\d+)_.*\.md$', fname, re.IGNORECASE)
            if m:
                n = int(m.group(1))
                if args.p_from <= n <= args.p_to:
                    md_files.append((n, os.path.join(md_dir, fname)))

    os.makedirs(out_dir, exist_ok=True)

    # Logo
    if args.logo:
        LOGO_PATH = args.logo
    else:
        for candidate in [
            os.path.join(md_dir, 'goal-logo-white.png'),
            os.path.join(os.path.dirname(md_dir), 'goal-logo-white.png'),
        ]:
            if os.path.exists(candidate):
                LOGO_PATH = candidate; break
    if not LOGO_PATH or not os.path.exists(LOGO_PATH):
        print("AVISO: goal-logo-white.png não encontrado — PDFs sem logotipo.")

    if not md_files:
        print("ERROR: Nenhum arquivo Pxx_*.md encontrado."); sys.exit(1)

    print(f"\n{len(md_files)} arquivo(s) encontrado(s). Gerando PDFs...\n")
    ok, fail = 0, []
    for p_num, md_path in md_files:
        fname = os.path.basename(md_path)
        try:
            out_path = build_pdf(md_path, out_dir, log_fn=print)
            print(f"  ✓ {os.path.basename(out_path)}")
            ok += 1
        except Exception as e:
            print(f"  ✗ {fname}: {e}")
            fail.append(fname)

    print(f"\nConcluído: {ok}/{len(md_files)}")
    if fail: print(f"Falhos: {', '.join(fail)}")
    print(f"Saída: {out_dir}\n")

# === Añadido para UI runner: pipeline sin traducción ===
def run_pipeline(md_dir='', md_file='', logo_path='', out_dir='', p_from=1, p_to=99, log_fn=print):
    global LOGO_PATH
    if md_file:
        md_dir = os.path.dirname(os.path.abspath(md_file))
        out_dir = out_dir or md_dir
        md_files = []
        m = re.match(r'^P(\d+)', os.path.basename(md_file), re.IGNORECASE)
        if m:
            md_files = [(int(m.group(1)), md_file)]
    else:
        md_dir = (md_dir or '').rstrip('/')
        out_dir = out_dir or md_dir
        md_files = []
        for fname in sorted(os.listdir(md_dir)):
            m = re.match(r'^P(\d+)_.*\.md$', fname, re.IGNORECASE)
            if m:
                n = int(m.group(1))
                if p_from <= n <= p_to:
                    md_files.append((n, os.path.join(md_dir, fname)))

    if not md_dir or not os.path.isdir(md_dir):
        raise FileNotFoundError(f"Carpeta inválida: {md_dir}")
    os.makedirs(out_dir, exist_ok=True)

    LOGO_PATH = ''
    for candidate in [logo_path,
                      os.path.join(md_dir, 'goal-logo-white.png'),
                      os.path.join(os.path.dirname(md_dir), 'goal-logo-white.png')]:
        if candidate and os.path.exists(candidate):
            LOGO_PATH = candidate
            break
    if not LOGO_PATH:
        log_fn("AVISO: goal-logo-white.png no encontrado — PDFs sin logotipo.")

    if not md_files:
        raise RuntimeError("No se encontraron archivos Pxx_*.md en la carpeta.")

    log_fn(f"{len(md_files)} archivo(s) encontrados. Generando PDFs...")
    ok, fail = 0, []
    for p_num, md_path in md_files:
        fname = os.path.basename(md_path)
        try:
            out_path = build_pdf(md_path, out_dir, log_fn=log_fn)
            log_fn(f"  ✓ {os.path.basename(out_path)}")
            ok += 1
        except Exception as e:
            log_fn(f"  ✗ {fname}: {e}")
            fail.append(fname)

    if fail:
        log_fn(f"Fallaron: {', '.join(fail)}")
    log_fn(f"Concluido: {ok}/{len(md_files)}. Salida: {out_dir}")
    return {"ok": ok, "total": len(md_files), "out_dir": out_dir}


# Sobrescribimos main para usar run_pipeline
def main():
    parser = argparse.ArgumentParser(description='goalbus Quick Start PDF generator (PT)')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--md-dir', help='Carpeta con archivos Pxx_*.md en portugués')
    group.add_argument('--md', help='Archivo markdown individual')
    parser.add_argument('--logo', default='', help='Ruta a goal-logo-white.png')
    parser.add_argument('--out', default='', help='Carpeta de salida')
    parser.add_argument('--from', dest='p_from', type=int, default=1)
    parser.add_argument('--to', dest='p_to', type=int, default=99)
    args = parser.parse_args()

    summary = run_pipeline(md_dir=args.md_dir, md_file=args.md, logo_path=args.logo,
                           out_dir=args.out, p_from=args.p_from, p_to=args.p_to, log_fn=print)
    print(f"Resumen: {summary['ok']}/{summary['total']} ok. Salida: {summary['out_dir']}")


if __name__ == '__main__':
    main()
