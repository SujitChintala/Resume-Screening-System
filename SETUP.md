# Setup Guide - Resume Screening System

This guide provides detailed step-by-step instructions to set up and run the Resume Screening System on your local machine.

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

### Required Software
- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (Python package manager - usually comes with Python)
- **Git** (optional, for version control)

### Verify Installation

Open your terminal/command prompt and verify installations:

```bash
# Check Python version
python --version
# or
python3 --version

# Check pip version
pip --version
# or
pip3 --version
```

Expected output: Python 3.8.x or higher

## 🔧 Installation Steps

### Step 1: Download/Clone the Project

**Option A: Clone with Git**
```bash
git clone <repository-url>
cd Resume-Screening-Project
```

**Option B: Download ZIP**
1. Download the project ZIP file
2. Extract to your desired location
3. Navigate to the project folder

### Step 2: Create a Virtual Environment (Recommended)

Creating a virtual environment isolates project dependencies.

**On Windows:**
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate
```

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

You should see `(venv)` prefix in your terminal when activated.

### Step 3: Install Dependencies

With the virtual environment activated, install required packages:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Flask-CORS (cross-origin support)
- Pandas (data manipulation)
- NumPy (numerical computing)
- Scikit-learn (machine learning)
- Werkzeug (WSGI utility)

**Installation may take 2-5 minutes depending on your internet speed.**

### Step 4: Create Model Directory

Create a folder to store trained models:

**On Windows:**
```powershell
mkdir model
```

**On macOS/Linux:**
```bash
mkdir model
```

### Step 5: Verify Dataset

Ensure `UpdatedResumeDataSet.csv` is in the project root directory.

```
Resume-Screening-Project/
├── UpdatedResumeDataSet.csv  ← Should be here
├── train_model.py
├── app.py
└── ...
```

## 🎯 Training the Model

### Step 1: Run Training Script

Execute the training script to train the ML model:

```bash
python train_model.py
```

**Expected Output:**
```
==================================================
Resume Screening Model Training
==================================================

Loading dataset...
Dataset shape: (962, 2)
Categories found: ['Data Science' 'HR' 'Advocate' ...]

Cleaning resume texts...
Splitting data into train and test sets...
Training set size: 769
Test set size: 193

Vectorizing text using TF-IDF...
TF-IDF feature shape: (769, 1500)

Training Multinomial Naive Bayes classifier...
Making predictions on test set...

==================================================
Model Accuracy: 98.45%
==================================================

Classification Report:
...

✓ Model saved successfully to 'model/' directory

==================================================
Training completed successfully!
==================================================
```

**Training Time:** 10-30 seconds (depending on your CPU)

### Step 2: Verify Model Files

After training, check that these files were created:

```
model/
├── resume_classifier.pkl
├── tfidf_vectorizer.pkl
└── label_encoder.pkl
```

## 🚀 Running the Application

### Step 1: Start Flask Server

```bash
python app.py
```

**Expected Output:**
```
============================================================
Resume Screening Application
============================================================

✓ Models loaded successfully

Starting Flask server...
Access the application at: http://localhost:5000
============================================================

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
```

### Step 2: Access the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

You should see the Resume Screening System interface.

### Step 3: Test the Application

1. **Paste Resume Text** or **Upload a Text File**
2. Click **"Analyze Resume"**
3. View the predicted job category and confidence score

## 🧪 Testing the System

### Sample Resume Text

Try this sample Data Science resume:

```
Skills: Python, Machine Learning, Deep Learning, TensorFlow, 
PyTorch, Pandas, NumPy, Scikit-learn, Data Analysis, 
Statistical Modeling, SQL, Data Visualization

Experience:
- Developed machine learning models for predictive analytics
- Built neural networks using TensorFlow and Keras
- Performed data analysis and created dashboards
- Implemented recommendation systems

Education:
Bachelor's in Computer Science
Master's in Data Science
```

Expected Result: **Data Science** (90%+ confidence)

## 🛠️ Troubleshooting

### Issue: "Model files not found"

**Solution:** Run the training script first:
```bash
python train_model.py
```

### Issue: "Port 5000 already in use"

**Solution:** Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

Then access: `http://localhost:5001`

### Issue: "ModuleNotFoundError"

**Solution:** Ensure virtual environment is activated and dependencies are installed:
```bash
# Activate virtual environment
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Dataset not found"

**Solution:** Ensure `UpdatedResumeDataSet.csv` is in the project root directory.

### Issue: Python command not found

**Solution:** Try using `python3` instead of `python`:
```bash
python3 train_model.py
python3 app.py
```

### Issue: Permission denied (Linux/macOS)

**Solution:** Use `sudo` or check file permissions:
```bash
chmod +x train_model.py
chmod +x app.py
```

## 🔄 Retraining the Model

To retrain with updated data:

1. **Update Dataset**: Add new resume samples to `UpdatedResumeDataSet.csv`
2. **Delete Old Models**: Remove files from `model/` directory
3. **Retrain**: Run `python train_model.py`
4. **Restart App**: Stop and restart `app.py`

## 🌐 Deployment (Optional)

### Local Network Access

To access from other devices on your network:

1. Find your IP address:
   - Windows: `ipconfig`
   - macOS/Linux: `ifconfig` or `ip addr`

2. Access from other devices: `http://<your-ip>:5000`

### Production Deployment

For production deployment, consider:
- **Gunicorn** (WSGI server): `pip install gunicorn`
- **Nginx** (reverse proxy)
- **Cloud platforms**: Heroku, AWS, Google Cloud, Azure
- Set `debug=False` in `app.py`

## 📦 Project File Checklist

Before running, ensure you have:

- ✅ `UpdatedResumeDataSet.csv` - Dataset file
- ✅ `train_model.py` - Training script
- ✅ `app.py` - Flask application
- ✅ `requirements.txt` - Dependencies
- ✅ `templates/index.html` - Frontend HTML
- ✅ `static/style.css` - Styling
- ✅ `static/script.js` - JavaScript
- ✅ `model/` directory - For storing trained models
- ✅ Virtual environment activated

## 💡 Tips for Success

1. **Always activate virtual environment** before running commands
2. **Train model before starting app** - models must exist first
3. **Use modern browser** - Chrome, Firefox, Edge (latest versions)
4. **Check console for errors** - Both terminal and browser console
5. **Keep terminal open** - Don't close the terminal running Flask

## 🆘 Getting Help

If you encounter issues:

1. Check the error message in the terminal
2. Verify all installation steps were completed
3. Ensure Python version is 3.8+
4. Check browser console for frontend errors (F12)
5. Verify all files are in correct locations

## ✅ Quick Start Summary

```bash
# 1. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create model directory
mkdir model

# 4. Train the model
python train_model.py

# 5. Run the application
python app.py

# 6. Open browser
# Navigate to http://localhost:5000
```

## 🎉 Success Indicators

You'll know setup was successful when:
- ✅ Training script completes without errors
- ✅ Model files appear in `model/` directory
- ✅ Flask server starts without errors
- ✅ Web interface loads at localhost:5000
- ✅ Resume analysis returns predictions

---

**Congratulations!** 🎊 Your Resume Screening System is now ready to use!

For more information, see [README.md](README.md)
