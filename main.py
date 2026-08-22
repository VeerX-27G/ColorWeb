import numpy as np
import PIL.Image as Image
from PIL import UnidentifiedImageError
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('index.html')

    if 'file' not in request.files:
        return render_template('index.html', error='Please select an image to upload.')

    file = request.files['file']
    if not file.filename:
        return render_template('index.html', error='Please select an image to upload.')

    try:
        # Open the image with Pillow and convert it to RGB.
        img = Image.open(file).convert('RGB')
    except (UnidentifiedImageError, OSError):
        return render_template('index.html', error='The selected file is not a valid image.')

    # Optional: Resize image to speed up NumPy processing
    img.thumbnail((300, 300))

    # 2. Convert PIL image to a 3D NumPy array (height, width, channels)
    img_array = np.array(img)

    # 3. Reshape 3D array to a 2D array of pixels: (num_pixels, 3)
    pixels = img_array.reshape(-1, 3)

    # 4. Find unique RGB colors and their counts using NumPy
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)

    # 5. Sort counts in descending order and select top 10 index positions
    top_10_indices = np.argsort(counts)[::-1][:10]
    top_10_colors = unique_colors[top_10_indices]

    # 6. Convert NumPy RGB arrays to HEX strings
    hex_colors = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in top_10_colors]

    return render_template('upload.html', colors=hex_colors)

if __name__ == '__main__':
    app.run(debug=True)