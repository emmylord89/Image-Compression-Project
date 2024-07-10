from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
import os
import numpy as np
from src.utils import load_image, save_image
from src.compression import compress_image, decompress_image

# Create the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    """
    Render the main page.
    
    Returns:
    - str: HTML content of the main page.
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle image upload, compression, and return the compressed image.
    
    Returns:
    - response: compressed image file as attachment.
    """
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        # Save the uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Load and compress the image
        image_array = load_image(filepath)
        compressed_image = compress_image(image_array)
        
        # Save the compressed image
        compressed_path = os.path.join(app.config['UPLOAD_FOLDER'], 'compressed_' + filename)
        with open(compressed_path, 'wb') as f:
            f.write(compressed_image)
        
        return send_file(compressed_path, as_attachment=True)

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Run the Flask development server
    app.run(debug=True)
