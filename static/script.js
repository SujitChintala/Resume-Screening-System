// DOM Elements
const resumeText = document.getElementById('resumeText');
const fileInput = document.getElementById('fileInput');
const fileLabel = document.querySelector('.file-label');
const analyzeBtn = document.getElementById('analyzeBtn');
const clearBtn = document.getElementById('clearBtn');
const resultsCard = document.getElementById('resultsCard');
const resultsContent = document.getElementById('resultsContent');
const loadingSpinner = document.getElementById('loadingSpinner');

// API Base URL
const API_URL = 'http://localhost:5000/api';

// Global variable to store uploaded file
let uploadedFile = null;

// File upload handler
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        uploadedFile = file;
        
        // Check if it's a PDF
        if (file.name.toLowerCase().endsWith('.pdf')) {
            resumeText.value = `PDF file selected: ${file.name}\n\nClick "Analyze Resume" to process this PDF file.`;
            resumeText.disabled = true;
            fileLabel.textContent = `📎 ${file.name}`;
            fileLabel.style.borderColor = '#667eea';
            fileLabel.style.color = '#667eea';
        } else {
            // For text files, read and display content
            const reader = new FileReader();
            reader.onload = (event) => {
                resumeText.value = event.target.result;
                resumeText.disabled = false;
                fileLabel.textContent = `📎 ${file.name}`;
                fileLabel.style.borderColor = '#667eea';
                fileLabel.style.color = '#667eea';
            };
            reader.readAsText(file);
        }
    }
});

// Clear button handler
clearBtn.addEventListener('click', () => {
    resumeText.value = '';
    resumeText.disabled = false;
    fileInput.value = '';
    uploadedFile = null;
    fileLabel.textContent = '📎 Or upload a file (PDF/TXT)';
    fileLabel.style.borderColor = '#ccc';
    fileLabel.style.color = '#666';
    resultsCard.style.display = 'none';
});

// Analyze button handler
analyzeBtn.addEventListener('click', async () => {
    // Check if file is uploaded
    if (uploadedFile) {
        await analyzeResumeFile(uploadedFile);
    } else {
        const text = resumeText.value.trim();
        
        if (!text) {
            showError('Please enter or upload resume text');
            return;
        }
        
        await analyzeResumeText(text);
    }
});

// Analyze resume from text
async function analyzeResumeText(text) {
    try {
        // Show loading spinner
        loadingSpinner.style.display = 'block';
        resultsCard.style.display = 'none';
        analyzeBtn.disabled = true;
        
        // Make API request
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                resume_text: text
            })
        });
        
        const data = await response.json();
        
        // Hide loading spinner
        loadingSpinner.style.display = 'none';
        analyzeBtn.disabled = false;
        
        if (data.success) {
            displayResults(data);
        } else {
            showError(data.error || 'An error occurred while analyzing the resume');
        }
        
    } catch (error) {
        console.error('Error:', error);
        loadingSpinner.style.display = 'none';
        analyzeBtn.disabled = false;
        showError('Failed to connect to the server. Please ensure the Flask server is running.');
    }
}

// Analyze resume from file
async function analyzeResumeFile(file) {
    try {
        // Show loading spinner
        loadingSpinner.style.display = 'block';
        resultsCard.style.display = 'none';
        analyzeBtn.disabled = true;
        
        // Create FormData for file upload
        const formData = new FormData();
        formData.append('file', file);
        
        // Make API request
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        // Hide loading spinner
        loadingSpinner.style.display = 'none';
        analyzeBtn.disabled = false;
        
        if (data.success) {
            displayResults(data);
        } else {
            showError(data.error || 'An error occurred while analyzing the resume');
        }
        
    } catch (error) {
        console.error('Error:', error);
        loadingSpinner.style.display = 'none';
        analyzeBtn.disabled = false;
        showError('Failed to connect to the server. Please ensure the Flask server is running.');
    }
}

// Display results function
function displayResults(data) {
    const { predicted_category, confidence, top_predictions } = data;
    
    let html = `
        <div class="result-main">
            <div class="result-category">
                ${predicted_category}
            </div>
            <div class="result-confidence">
                Confidence: ${confidence}%
            </div>
        </div>
    `;
    
    if (top_predictions && top_predictions.length > 0) {
        html += `
            <div class="top-predictions">
                <h3>Top 3 Predictions:</h3>
        `;
        
        top_predictions.forEach((pred, index) => {
            html += `
                <div class="prediction-item">
                    <span class="prediction-name">
                        ${index + 1}. ${pred.category}
                    </span>
                    <span class="prediction-confidence">
                        ${pred.confidence.toFixed(2)}%
                    </span>
                </div>
            `;
        });
        
        html += `</div>`;
    }
    
    resultsContent.innerHTML = html;
    resultsCard.style.display = 'block';
    
    // Smooth scroll to results
    resultsCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Show error function
function showError(message) {
    const html = `
        <div class="error-message">
            ⚠️ ${message}
        </div>
    `;
    
    resultsContent.innerHTML = html;
    resultsCard.style.display = 'block';
    
    // Smooth scroll to error
    resultsCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Check server health on page load
window.addEventListener('load', async () => {
    try {
        const response = await fetch(`${API_URL}/health`);
        const data = await response.json();
        
        if (!data.models_loaded) {
            console.warn('Models not loaded on server');
        }
    } catch (error) {
        console.error('Server health check failed:', error);
    }
});
