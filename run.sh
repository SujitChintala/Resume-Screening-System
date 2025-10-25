#!/bin/bash

echo "========================================"
echo "Resume Screening System - Quick Start"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Install requirements if needed
echo "Checking dependencies..."
pip install -q -r requirements.txt
echo ""

# Check if model exists
if [ ! -f "model/resume_classifier.pkl" ]; then
    echo "Model not found. Training model..."
    echo "This may take a minute..."
    python train_model.py
    echo ""
fi

# Start the application
echo "Starting Resume Screening System..."
echo ""
echo "Access the application at: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo ""
python app.py
