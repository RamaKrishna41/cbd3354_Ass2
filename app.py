import os
from flask import Flask, request, jsonify, send_from_directory
from google.cloud import aiplatform
import google.generativeai as genai

app = Flask(__name__)

API_KEY = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

genai.configure(api_key=API_KEY)

@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    try:
        response = genai.generate_text(prompt=prompt)
        # Extract the result from the Completion object
        generated_text = response.result if hasattr(response, 'result') else 'No result found in response'
        return jsonify({'response': generated_text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
