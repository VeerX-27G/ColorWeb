# ColorWeb

A small Flask web app that extracts the dominant colors from an image. Upload a picture, and ColorWeb returns the 10 most frequent colors as HEX codes, shown as a palette of swatches.

## Features

- Upload any common image format (PNG, JPG, GIF, WebP, etc.) through a simple form
- Shows the top 10 most frequent colors as labeled color cards
- Friendly error messages for a missing file or a file that isn't a valid image
- Responsive layout that works on desktop and mobile

## How it works

1. The uploaded file is opened with **Pillow** and converted to RGB.
2. The image is downscaled to fit within 300×300 pixels so processing stays fast.
3. **NumPy** converts the image to an array and flattens it to a list of `(R, G, B)` pixels.
4. `np.unique` counts how often each exact RGB value appears.
5. The 10 most frequent values are converted to HEX strings (e.g. `#6757e8`) and rendered by **Jinja2** templates.

> Note: colors are counted as exact RGB values, not clustered. For photos with lots of gradients, the top 10 may contain several very similar shades.

## Tech stack

| Layer | Tools |
| --- | --- |
| Backend | Python, Flask |
| Image processing | Pillow, NumPy |
| Frontend | HTML (Jinja2 templates), CSS |

## Project structure

```
ColorWeb/
├── main.py              # Flask app: routes and color extraction logic
├── templates/
│   ├── index.html       # Upload form (also shows errors and results)
│   └── upload.html      # Results page with the extracted palette
├── static/
│   └── style.css        # Styling
├── pyproject.toml       # Project metadata and dependencies
├── uv.lock              # Locked dependency versions (uv)
└── .github/workflows/   # GitHub Pages workflow
```

## Getting started

### Prerequisites

- Python 3.14 or newer (as set in `pyproject.toml`)
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

```bash
git clone https://github.com/VeerX-27G/ColorWeb.git
cd ColorWeb
```

**With uv:**

```bash
uv sync
uv run main.py
```

**With pip:**

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install flask numpy pillow
python main.py
```

Then open <http://127.0.0.1:5000> in your browser.

## Usage

1. Open the home page.
2. Choose an image and click **Upload & Process**.
3. View the palette of the 10 most common colors with their HEX codes.
4. Click **Upload another image** to try again.

## Routes

| Route | Methods | Description |
| --- | --- | --- |
| `/` | GET | Home page with the upload form |
| `/upload` | GET, POST | POST processes the image and renders the palette; GET returns to the form |

## Notes

- `main.py` runs the app with `debug=True`, which is meant for local development only. Turn it off before deploying anywhere public.
- Uploaded images are processed in memory and are not saved to disk.
