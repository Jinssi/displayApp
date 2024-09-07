from flask import Flask, render_template, jsonify, send_from_directory
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Directory containing images
IMAGE_DIR = '/home/aapo/appAll/displayImages'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_images', methods=['GET'])
def fetch_images():
    # List all image files in the directory
    images = [f for f in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f))]
    return jsonify(images)

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_DIR, filename)

# Define the missing routes
@app.route('/fetch_posts', methods=['GET'])
def fetch_posts():
    # Placeholder for fetching posts logic
    return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)