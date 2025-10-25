# Setup Guide - Resume Screening System

Quick guide to set up and run the Resume Screening System.

## 📋 Prerequisites

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** (comes with Python)

Verify installation:
```bash
python --version  # Should show 3.8+
pip --version
```

## � Quick Start

### 1. Clone/Download Project
```bash
git clone <repository-url>
cd Resume-Screening-Project
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create Model Directory
```bash
mkdir model
```

## 🎯 Train the Model

```bash
python train_model.py
```

This trains the ML model and saves it to the `model/` directory (takes ~30 seconds).

## 🌐 Run the Application

```bash
python app.py
```

Open your browser and go to: **http://localhost:5000**

### Usage
1. Paste resume text or upload a PDF/TXT file
2. Click "Analyze Resume"
3. View predicted job category and confidence score

---

## ⚡ One-Command Setup 

### Windows

```bash
.\run.bat
```

### Mac/Linux

```bash
.\run.sh
```

This automatically sets up environment, installs dependencies, trains model, and starts the app.

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| "Model files not found" | Run `python train_model.py` first |
| "Port 5000 in use" | Change port in `app.py` to 5001 |
| "ModuleNotFoundError" | Activate venv and run `pip install -r requirements.txt` |
| Python not found | Try `python3` instead of `python` |

## 📝 Common Tasks

**Retrain Model:**
```bash
python train_model.py
```


**Need help?** Check [README.md](README.md) for more details.
