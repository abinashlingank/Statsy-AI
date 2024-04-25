from flask import Flask, request, jsonify, send_from_directory
import subprocess
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) 

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv'))
        subprocess.run(['python3', 'run_llama.py'])
        return jsonify({'message': 'File uploaded and processed successfully'})

@app.route('/get_images', methods=['GET'])
def get_images():
    image_files = os.listdir('output')
    return jsonify({'images': image_files})

# Route to serve static files from the 'output' directory
@app.route('/output/<path:filename>')
def serve_static(filename):
    return send_from_directory('output', filename)

if __name__ == '__main__':
    
    # Get the current working directory
    current_directory = os.getcwd()

    UPLOAD_FOLDER = current_directory

    # Set the Flask app's upload folder configuration
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    
    # Run the Flask app
    app.run(debug=True, use_reloader=False)
