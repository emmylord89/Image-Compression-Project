from flask import Blueprint, render_template, request, send_from_directory, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
from src.utils import load_image, save_image
from src.compression import compress_image
from src.decompression import decompress_image

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join('uploads', filename)
            file.save(filepath)

            # Load and compress the image
            image_array = load_image(filepath)
            compressed_image = compress_image(image_array)

            # Save the compressed data
            compressed_filepath = os.path.join('uploads', 'compressed_' + filename + '.bin')
            with open(compressed_filepath, 'wb') as f:
                f.write(compressed_image)

            return redirect(url_for('main.download_file', filename='compressed_' + filename + '.bin'))

    return render_template('index.html')

@bp.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory('uploads', filename)
