# Quick Starts goalbus — v2.1.0

Genera PDFs y DOCXs a partir de Markdown de Quick Starts y los opera via una UI local. El texto se toma exactamente del Markdown, sin traducciones.

## Contenido

| Archivo | Descripción |
|---|---|
| `goalbus_pdf_pt.py` | Motor de generación (PDF reportlab + DOCX + conversión a PDF) |
| `ui_runner.py` | Backend Flask de la UI local |
| `ui_runner.html` | Frontend de la UI local |
| `requirements.txt` | Dependencias Python |
| `test/` | Markdowns de prueba y archivos de referencia |

---

## Requisitos

### Python
- Python **3.9+**
- Dependencias (ver `requirements.txt`):

| Paquete | Para qué se usa |
|---|---|
| `flask` | Servidor de la UI local |
| `reportlab` | Generación de PDF desde Markdown |
| `python-docx` | Generación de archivos `.docx` |
| `Pillow` | Procesamiento de imágenes en PDF y DOCX |
| `lxml` | Procesamiento XML requerido por python-docx |
| `docx2pdf` | Conversión DOCX→PDF via Word (fallback si no hay LibreOffice) |

### Sistema (para conversión DOCX→PDF)
La opción `docx+pdf` convierte el DOCX a PDF después de generarlo. Usa **LibreOffice** en modo headless (sin interfaz, sin permisos, rápido). Si no está instalado, cae a Microsoft Word vía `docx2pdf`.

- **Recomendado:** [LibreOffice](https://www.libreoffice.org) — sin diálogos, sin permisos de automatización macOS
- **Alternativa:** Microsoft Word instalado en el equipo

---

## Instalación

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Windows (PowerShell)
```powershell
py -3 -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

Verificación (debe apuntar a `.venv`):
```bash
python -c "import sys; print(sys.executable)"
```

---

## UI local

Arranca en `http://127.0.0.1:1234`:
```bash
python ui_runner.py
```

### Qué permite la UI
- Seleccionar carpeta de Markdown
- Seleccionar logo (opcional)
- Crear carpeta de salida si no existe
- Elegir formato: **PDF** o **DOCX** (al seleccionar DOCX genera también el PDF automáticamente)
- Filtrar por documentos específicos con patrones flexibles (`P*`, `O1:O15`, `P1, P5`)
- Ver log de generación en tiempo real

Selectores de carpeta multiplataforma:
- **macOS:** AppleScript
- **Windows:** IFileOpenDialog via COM (soporta OneDrive y rutas Unicode)
- **Linux:** `zenity` si está disponible; si no, escribe la ruta manualmente

---

## CLI

### Generar desde una carpeta
```bash
python goalbus_pdf_pt.py --md-dir /ruta/a/markdowns/
```

### Generar desde un archivo
```bash
python goalbus_pdf_pt.py --md /ruta/a/P01_titulo.md
```

### Opciones

| Opción | Descripción | Default |
|---|---|---|
| `--md-dir` | Carpeta con archivos `Pxx_*.md` | — |
| `--md` | Archivo Markdown individual | — |
| `--out` | Carpeta de salida | misma que `--md-dir` |
| `--logo` | Ruta a `goal-logo-white.png` | búsqueda automática |
| `--from N` | Procesar desde el número N | 1 |
| `--to N` | Procesar hasta el número N | 99 |
| `--format` | Formato de salida: `pdf`, `docx`, `docx+pdf` | `pdf` |
| `--px-filter` | Filtro de documentos (ver sección Filtrado) | — |
| `--lang` | Idioma para etiquetas: `ES`, `EN`, `PT`, `FR`, `DE`, `IT`, `auto` | `auto` |

### Formatos de salida

| Formato | Qué genera | Requiere |
|---|---|---|
| `pdf` | PDF via reportlab (fiel al diseño) | — |
| `docx` | Solo el archivo Word `.docx` | — |
| `docx+pdf` | `.docx` + `.pdf` convertido desde el DOCX | LibreOffice o Word |

```bash
# Solo PDF (reportlab)
python goalbus_pdf_pt.py --md-dir ./docs/ --format pdf

# Solo DOCX
python goalbus_pdf_pt.py --md-dir ./docs/ --format docx

# DOCX y también PDF (fiel al Word)
python goalbus_pdf_pt.py --md-dir ./docs/ --format docx+pdf
```

---

## Filtrado de archivos

Tanto en la UI como en CLI (`--px-filter`), se puede filtrar qué documentos generar.

### Sintaxis

| Patrón | Descripción | Ejemplo |
|---|---|---|
| `P*` | Todos los documentos con prefijo `P` | `P*` |
| `P1` | Exactamente ese número | `P1` |
| `P1:P15` | Rango inclusivo | `P1:P15` |
| Combinaciones | Separadas por `,` | `P1, P5, O1:O10` |

### Ejemplos
```bash
--px-filter "P*"
--px-filter "P1:P15,O1:O15"
--px-filter "O1,O7:O16,R17:R20,R21"
```

> Los prefijos no están limitados a `P`; se soporta cualquier combinación de letras (`O`, `R`, `ABC`, etc.).

---

## Imágenes (`ref:`)

Inserta imágenes en el Markdown con una línea `ref:`. Funciona tanto en PDF como en DOCX.

```markdown
ref: nombre_imagen.png
ref: nombre_imagen
ref: imagen_browser | size=full
ref: login | size=compact
ref: captura_larga | split=2
ref: diagrama | size=compact(2x5)
ref: icono | compact(3x3)
ref: captura_ancha | size=compact(x8)
ref: captura_alta | size=compact(10x)
```

### Opciones de tamaño

| Opción | Comportamiento |
|---|---|
| `size=auto` | Automático según proporción (default) |
| `size=full` | Ancho máximo útil |
| `size=compact` | Ancho reducido, ideal para diálogos o capturas focales |
| `size=compact(AxW)` | Alto y/o ancho fijos en cm (`compact(2x5)`, `compact(x8)`, `compact(10x)`) |
| `split=N` | Divide la imagen en N bloques verticales (1–6) |

### Dónde busca las imágenes

La carpeta base es la indicada en `--md-dir` o en la UI. Para `P1_titulo.md` busca en subcarpetas `P1/` y `P01/`. Sin extensión, prueba `.png`, `.jpg`, `.jpeg` en orden.

---

## Problemas comunes

**`ModuleNotFoundError`**
```bash
pip install -r requirements.txt
```

**La UI no abre el selector de carpeta en Linux**
Instala `zenity`:
```bash
sudo apt install zenity   # Debian/Ubuntu
sudo dnf install zenity   # Fedora
```

**`docx+pdf` falla o produce un PDF con layout incorrecto**
- Instala LibreOffice desde [libreoffice.org](https://www.libreoffice.org) — es el método recomendado.
- Si solo tienes Word (macOS), puede aparecer un diálogo de permisos la primera vez. Acepta en **Ajustes del Sistema › Privacidad y seguridad › Automatización** y permite que Terminal controle Microsoft Word.

**`ensurepip` falla al crear el venv**
```bash
python3 -m ensurepip --upgrade
python3 -m venv .venv
```

**`pip` instala pero Python no encuentra los paquetes**
Asegúrate de haber activado el venv (`source .venv/bin/activate`) y de que `python` apunte a `.venv`. Si usas conda, ejecuta `conda deactivate` primero.

**Rutas con espacios**
Usa comillas:
```bash
python goalbus_pdf_pt.py --md-dir "/ruta con espacios/markdowns/"
```
