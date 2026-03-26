# Quick Starts goalbus

Proyecto para generar PDFs a partir de Markdown de Quick Starts y operarlos via una UI local. No se realizan traducciones: el texto del PDF se toma exactamente del Markdown.

## Contenido
- Generador de PDF: `goalbus_pdf_pt.py`
- UI local (backend+frontend): `ui_runner.py` + `ui_runner.html`
- Assets: logos `goal-logo-*.png`, Markdown en `test/`, PDFs en `Español/` y `Portugues/`
- Documento de plan (capturas desde video): `output/doc/plan_captura_imagenes_quickstarts.docx`

## Requisitos
- Python 3.9+
- Dependencias Python:
  - `flask`
  - `reportlab`

Instalacion (recomendado con venv):
```bash
python -m venv .venv
source .venv/bin/activate
pip install flask reportlab
```

Windows:
```bat
python -m venv .venv
.\.venv\Scripts\activate
pip install flask reportlab
```

## Uso rapido (UI)
Arranca backend+frontend en `http://127.0.0.1:1234`:
```bash
python ui_runner.py
```

La UI permite:
- Elegir carpeta de Markdown
- Elegir logo (opcional)
- Crear carpeta de salida (si no existe)
- Ejecutar generacion y ver logs

Seletores multiplataforma:
- macOS: AppleScript
- Windows: PowerShell + Shell.Application
- Linux: `zenity` (si esta disponible). Si no, escribe la ruta manualmente.

## Uso directo (CLI)
Generar PDFs desde un directorio de Markdown:
```bash
python goalbus_pdf_pt.py --md-dir /ruta/a/markdowns
```

Generar desde un archivo:
```bash
python goalbus_pdf_pt.py --md /ruta/a/P01_*.md
```

Opciones:
- `--logo` ruta a `goal-logo-white.png`
- `--out` carpeta de salida
- `--from` y `--to` para rango de Pxx

## Salida
Cada PDF se guarda con el mismo nombre del Markdown (solo cambia la extension a `.pdf`).

## Notas de formato
- Los encabezados `##` se renderizan con barra lateral y numero de seccion.
- El texto no se traduce ni se reescribe: se respeta el Markdown original.

## Referencias de imagen (`ref:`)
Puedes insertar imagenes en el PDF escribiendo una linea independiente en el Markdown:

```md
ref: Captura de pantalla 2026-03-26 a las 11.27.55.png
```

Tambien se admite referencia sin extension:

```md
ref: imagen1
```

Reglas de resolucion:
- La carpeta base es la carpeta de Markdown seleccionada por el usuario en la UI (o `--md-dir` en CLI).
- Para un archivo `P1_*.md`, se busca la imagen en subcarpetas `P1/` y `P01/` (fallback).
- Para un archivo `P12_*.md`, se busca en `P12/`.
- Si la referencia no tiene extension, se intenta en orden: `.png`, `.jpg`, `.jpeg`.

Comportamiento en PDF:
- La imagen se inserta centrada, manteniendo proporcion.
- Se limita ancho/alto para no romper la maquetacion ni invadir header/footer.
- No se escala hacia arriba (sin `upscale`) para preservar nitidez percibida.
- El bloque de imagen no se corta entre paginas.
- Si falta la imagen o la referencia es invalida, se agrega un aviso visible en el PDF y se registra warning en logs, sin detener la generacion.

## Plan de automatizacion de capturas (video + OCR)
Se genero un plan tecnico para automatizar capturas desde video y agregar imagenes a los Quick Starts sin alterar el texto:
- `output/doc/plan_captura_imagenes_quickstarts.docx`

## Problemas comunes
- `ModuleNotFoundError: No module named 'flask'`: instala dependencias con `pip install flask reportlab`.
- Rutas con espacios: usa comillas en el comando.
