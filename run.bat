@echo off
echo ========================================
echo Resume Screening System - Quick Start
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate
echo.

REM Install requirements if needed
echo Checking dependencies...
pip install -q -r requirements.txt
echo.

REM Check if model exists
if not exist "model\resume_classifier.pkl" (
    echo Model not found. Training model...
    echo This may take a minute...
    python train_model.py
    echo.
)

REM Start the application
echo Starting Resume Screening System...
echo.
echo Access the application at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
