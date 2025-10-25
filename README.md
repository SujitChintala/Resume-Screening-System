# Resume Screening System

An intelligent AI-powered resume screening application that automatically classifies resumes into job categories using Machine Learning and Natural Language Processing.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Overview

This project implements an end-to-end resume screening system that:
- Automatically classifies resumes into different job categories
- Uses TF-IDF vectorization and Multinomial Naive Bayes classifier
- Provides a clean and intuitive web interface
- Offers real-time predictions with confidence scores

## ✨ Features

- **Intelligent Classification**: Automatically categorizes resumes into job roles
- **High Accuracy**: Machine learning model trained on diverse resume dataset
- **Web Interface**: Simple and elegant frontend for easy interaction
- **Real-time Analysis**: Instant resume classification results
- **Confidence Scores**: Shows prediction confidence and top 3 matches
- **Text Processing**: Advanced NLP techniques for resume text cleaning
- **Easy to Use**: Upload text files or PDFs or paste resume content directly

## 🏗️ Project Structure

```
Resume-Screening-Project/
│
├── app.py                      # Flask web application
├── train_model.py              # Model training script
├── requirements.txt            # Python dependencies
├── UpdatedResumeDataSet.csv   # Training dataset
├── .gitignore                 # Git ignore rules
│
├── model/                     # Trained model files (generated)
│   ├── resume_classifier.pkl
│   ├── tfidf_vectorizer.pkl
│   └── label_encoder.pkl
│
├── templates/                 # HTML templates
│   └── index.html
│
└── static/                    # Static assets
    ├── style.css
    └── script.js
```

## 🚀 Technologies Used

**Backend:**
- Python 3.8+
- Flask (Web framework)
- Scikit-learn (Machine Learning)
- Pandas & NumPy (Data processing)
- NLTK/Regex (Text preprocessing)

**Frontend:**
- HTML5
- CSS3 (with modern gradients and animations)
- Vanilla JavaScript (ES6+)

**Machine Learning:**
- TF-IDF Vectorization
- Multinomial Naive Bayes Classifier
- Label Encoding

## 📊 Model Performance

The model is trained on a comprehensive dataset of resumes across multiple job categories including:
- Data Science
- Web Development
- Java Developer
- Python Developer
- HR
- And many more...

Expected accuracy: **95%+** (varies based on dataset)

## 🔧 Installation & Setup

Please refer to the [SETUP.md](SETUP.md) file for detailed installation and setup instructions.

## 📖 Usage

### Training the Model

```bash
python train_model.py
```

This will:
1. Load and preprocess the dataset
2. Train the classification model
3. Save the trained model files to `model/` directory

### Running the Application

```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

### Using the Web Interface

1. **Paste Resume Text**: Copy and paste resume content into the text area
2. **Or Upload File**: Click the upload button to select a `.txt` file
3. **Analyze**: Click the "Analyze Resume" button
4. **View Results**: See the predicted job category with confidence score

## 🔍 API Endpoints

### `POST /api/predict`
Predict resume category

**Request:**
```json
{
    "resume_text": "Your resume text here..."
}
```

**Response:**
```json
{
    "success": true,
    "predicted_category": "Data Science",
    "confidence": 95.5,
    "top_predictions": [
        {"category": "Data Science", "confidence": 95.5},
        {"category": "Machine Learning", "confidence": 3.2},
        {"category": "Python Developer", "confidence": 1.3}
    ]
}
```

### `GET /api/categories`
Get all available job categories

### `GET /api/health`
Check API health status

## 📁 Dataset

The project uses `UpdatedResumeDataSet.csv` containing:
- Multiple job categories
- Real-world resume samples
- Diverse skill sets and experience levels

## 🎯 How It Works

1. **Data Preprocessing**: Resume text is cleaned (remove URLs, special characters, etc.)
2. **Feature Extraction**: TF-IDF vectorization converts text to numerical features
3. **Classification**: Multinomial Naive Bayes predicts the job category
4. **Results**: Returns prediction with confidence scores

## 🛠️ Customization

### Adding New Categories
1. Add resume samples to the dataset
2. Retrain the model: `python train_model.py`
3. Restart the application

### Adjusting Model Parameters
Edit `train_model.py` to modify:
- TF-IDF parameters (`max_features`, `min_df`, `max_df`)
- Train/test split ratio
- Classification algorithm

## 📝 Project Highlights

This project demonstrates:
- ✅ End-to-end machine learning pipeline
- ✅ Web application development with Flask
- ✅ NLP and text processing techniques
- ✅ RESTful API design
- ✅ Modern frontend development
- ✅ Clean and maintainable code structure

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests


## 👨‍💻 Author

- GitHub: [SujitChintala](https://github.com/SujitChintala)
- LinkedIn: [Saai Sujit Chintala](https://www.linkedin.com/in/sujitchintala/)
- Email: sujitchintala@gmail.com

## 🙏 Acknowledgments

- Dataset: Resume dataset from various sources
- Libraries: Scikit-learn, Flask, and other open-source tools

<div align="center">

**⭐ Star this repository if you find it helpful!**

</div>