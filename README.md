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
  - `python-docx` (para salida `.docx`)

## Instalación (recomendado con venv)
### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows (PowerShell)
```bat
py -3 -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Si no tienes `requirements.txt`, instala directo:
```bash
python -m pip install flask reportlab python-docx
```

Verificación rápida (debe apuntar a `.venv`):
```bash
python -c "import sys; print(sys.executable)"
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
- Elegir formato de salida (`PDF` o `DOCX`) junto al botón Ejecutar
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
- `--format` formato de salida (`pdf` o `docx`)

## Salida
Cada archivo se guarda con el mismo nombre del Markdown, cambiando la extension segun formato:
- `.pdf` si `--format pdf` (default)
- `.docx` si `--format docx`

## Notas de formato
- Los encabezados `##` se renderizan con barra lateral y numero de seccion.
- El texto no se traduce ni se reescribe: se respeta el Markdown original.

## Referencias de imagen (`ref:`)
Puedes insertar imagenes en una linea independiente del Markdown. Aplica tanto para salida `PDF` como `DOCX`.

```md
ref: Captura de pantalla 2026-03-26 a las 11.27.55.png
```

Tambien se admite referencia sin extension:

```md
ref: imagen1
```

### Sintaxis exacta

```md
ref: <nombre_imagen> [| <opcion1>] [| <opcion2>]
```

Opciones soportadas (forma recomendada):
- `size=auto|full|compact`
- `split=N` con `N` entre `1` y `6`

Atajos tambien validos (equivalentes):
- `| auto`, `| full`, `| compact` (equivalente a `size=...`)
- `| 2`, `| 3` ... (equivalente a `split=...`)

### Ejemplos listos para copiar

```md
ref: imagen_browser | size=full
ref: login | size=compact
ref: captura_larga | split=2
ref: imagen_auto | size=auto | split=3
ref: Captura de pantalla 2026-03-26 a las 17.50.02 | compact
```

### Donde busca las imagenes

La carpeta base es la carpeta de Markdown seleccionada por el usuario en la UI (o `--md-dir` en CLI).

- Para un archivo `P1_*.md`, se busca la imagen en subcarpetas `P1/` y `P01/` (fallback).
- Para un archivo `P12_*.md`, se busca en `P12/`.
- Si la referencia no tiene extension, se intenta en orden: `.png`, `.jpg`, `.jpeg`.

### Como decide el tamaño (`size`)

`size=auto` (default) aplica estas reglas:
- Imagen panoramica/ancha (ejemplo: pantalla completa de navegador) -> tiende a `full`.
- Imagen focal o casi cuadrada/vertical (ejemplo: login/modal) -> tiende a `compact`.
- Si en auto el contenido quedara poco legible, el motor puede subir a `full`.

`size=full`:
- Usa el mayor ancho util posible, priorizando legibilidad.

`size=compact`:
- Usa ancho reducido y ahora tambien limita altura de forma analitica segun la relacion de aspecto.
- Resultado esperado: menos imagenes altas en `compact`, conservando proporcion (sin deformar).
- Si escribes `size=compact` de forma explicita, se respeta ese modo (no se promociona a `full`).

### Como funciona `split`

- `split` divide la imagen verticalmente en bloques consecutivos (de arriba hacia abajo).
- Cada bloque se coloca en orden y no se recorta entre paginas.
- Si no indicas `split` y la imagen es demasiado alta, el motor puede dividir automaticamente.
- Si indicas `split`, ese valor manual tiene prioridad sobre el split automatico.

Comportamiento de render:
- La imagen se inserta centrada, manteniendo proporcion.
- Se limita ancho/alto para no romper la maquetacion ni invadir header/footer.
- Se aplica un marco sutil y una sombra negra suave para mejorar separacion visual.
- No se escala hacia arriba (sin `upscale`) para preservar nitidez percibida.
- El bloque de imagen no se corta entre paginas.
- Si usas `split`, cada fragmento queda en bloques consecutivos y no se recorta.
- Si falta la imagen o la referencia es invalida, se agrega un aviso visible en la salida y se registra warning en logs, sin detener la generacion.

### Guia rapida de decision

- Usa `size=auto` como default.
- Usa `size=full` para pantallas completas con texto pequeño.
- Usa `size=compact` para capturas de dialogos o zonas puntuales.
- Usa `split=2` o `split=3` para capturas muy altas donde necesitas leer detalle sin reducir demasiado.

### Errores comunes (y como evitarlos)

- `ref:` debe ir solo en su linea.
- No uses rutas en `ref:` (`/` o `\\`); solo nombre de archivo.
- Si hay opciones invalidas, el sistema avisa en log y sigue con fallback seguro.

## Plan de automatizacion de capturas (video + OCR)
Se genero un plan tecnico para automatizar capturas desde video y agregar imagenes a los Quick Starts sin alterar el texto:
- `output/doc/plan_captura_imagenes_quickstarts.docx`

## Problemas comunes
- `ModuleNotFoundError: No module named 'flask'`: instala dependencias con `pip install flask reportlab python-docx`.
- Rutas con espacios: usa comillas en el comando.
- `ensurepip` falla al crear el venv: primero ejecuta `python3 -m ensurepip --upgrade` y luego vuelve a correr `python3 -m venv .venv`. Si persiste, reinstala Python desde python.org.
- `pip` instala pero `python` no encuentra paquetes: asegúrate de haber activado el venv y de que `python` apunte a `.venv` (verificación arriba). Si usas conda, ejecuta `conda deactivate` antes de activar el venv.
