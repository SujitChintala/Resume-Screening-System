"""
Resume Screening Web Application
Flask backend API for resume classification.
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import re
import os
from PyPDF2 import PdfReader
from werkzeug.utils import secure_filename
import pandas as pd

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Configuration
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

# Load trained model and preprocessing objects
MODEL_PATH = 'model/resume_classifier.pkl'
VECTORIZER_PATH = 'model/tfidf_vectorizer.pkl'
ENCODER_PATH = 'model/label_encoder.pkl'

# Global variables for model components
model = None
vectorizer = None
label_encoder = None


def load_models():
    """Load the trained models and preprocessing objects."""
    global model, vectorizer, label_encoder
    
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        
        with open(VECTORIZER_PATH, 'rb') as f:
            vectorizer = pickle.load(f)
        
        with open(ENCODER_PATH, 'rb') as f:
            label_encoder = pickle.load(f)
        
        print("✓ Models loaded successfully")
        return True
    except FileNotFoundError:
        print("✗ Model files not found. Please train the model first using train_model.py")
        return False


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text_from_pdf(file):
    """
    Extract text from PDF file.
    
    Args:
        file: FileStorage object
        
    Returns:
        str: Extracted text from PDF
    """
    try:
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")


def clean_resume_text(text):
    """
    Clean and preprocess resume text.
    
    Args:
        text (str): Raw resume text
        
    Returns:
        str: Cleaned resume text
    """
    # Remove URLs
    text = re.sub(r'http\S+\s*', ' ', text)
    # Remove RT and cc
    text = re.sub(r'RT|cc', ' ', text)
    # Remove hashtags
    text = re.sub(r'#\S+', '', text)
    # Remove mentions
    text = re.sub(r'@\S+', '  ', text)
    # Remove punctuations
    text = re.sub(r'[^\w\s]', ' ', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Convert to lowercase
    text = text.lower().strip()
    
    return text


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Predict the category of a resume.
    
    Accepts either:
    - JSON with "resume_text" field
    - File upload (PDF or TXT)
    
    Returns:
        JSON response with predicted category and probability
    """
    try:
        # Check if models are loaded
        if model is None or vectorizer is None or label_encoder is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded. Please train the model first.'
            }), 500
        
        resume_text = None
        
        # Check if it's a file upload
        if 'file' in request.files:
            file = request.files['file']
            
            if file.filename == '':
                return jsonify({
                    'success': False,
                    'error': 'No file selected'
                }), 400
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                
                # Extract text based on file type
                if filename.endswith('.pdf'):
                    resume_text = extract_text_from_pdf(file)
                else:  # .txt file
                    resume_text = file.read().decode('utf-8')
            else:
                return jsonify({
                    'success': False,
                    'error': 'Invalid file type. Only PDF and TXT files are allowed.'
                }), 400
        
        # Check if it's JSON data
        elif request.is_json:
            data = request.get_json()
            
            if not data or 'resume_text' not in data:
                return jsonify({
                    'success': False,
                    'error': 'No resume text provided'
                }), 400
            
            resume_text = data['resume_text']
        
        else:
            return jsonify({
                'success': False,
                'error': 'Invalid request format'
            }), 400
        
        if not resume_text or not resume_text.strip():
            return jsonify({
                'success': False,
                'error': 'Resume text is empty'
            }), 400
        
        # Clean and preprocess the text
        cleaned_text = clean_resume_text(resume_text)
        
        # Vectorize the text
        text_vectorized = vectorizer.transform([cleaned_text])
        
        # Make prediction
        prediction = model.predict(text_vectorized)[0]
        prediction_proba = model.predict_proba(text_vectorized)[0]
        
        # Get category name
        category = label_encoder.inverse_transform([prediction])[0]
        confidence = float(max(prediction_proba)) * 100
        
        # Get top 3 predictions
        top_3_indices = prediction_proba.argsort()[-3:][::-1]
        top_3_predictions = [
            {
                'category': label_encoder.inverse_transform([idx])[0],
                'confidence': float(prediction_proba[idx]) * 100
            }
            for idx in top_3_indices
        ]
        
        return jsonify({
            'success': True,
            'predicted_category': category,
            'confidence': round(confidence, 2),
            'top_predictions': top_3_predictions
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get all available job categories."""
    try:
        if label_encoder is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded'
            }), 500
        
        categories = label_encoder.classes_.tolist()
        
        return jsonify({
            'success': True,
            'categories': categories
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if the API is running and models are loaded."""
    models_loaded = (model is not None and 
                     vectorizer is not None and 
                     label_encoder is not None)
    
    return jsonify({
        'status': 'running',
        'models_loaded': models_loaded
    })


if __name__ == '__main__':
    print("\n" + "="*60)
    print("Resume Screening Application")
    print("="*60 + "\n")
    
    # Load models
    models_loaded = load_models()
    
    if not models_loaded:
        print("\n⚠ Warning: Models not loaded. Please train the model first.")
        print("Run: python train_model.py\n")
    
    print("\nStarting Flask server...")
    print("Access the application at: http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
