"""
Resume Screening Model Training Script
This script trains a machine learning model to classify resumes into different job categories.
"""

import pandas as pd
import numpy as np
import pickle
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
warnings.filterwarnings('ignore')


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


def load_and_prepare_data(csv_path):
    """
    Load and prepare the dataset.
    
    Args:
        csv_path (str): Path to the CSV file
        
    Returns:
        tuple: X (features), y (labels), label_encoder
    """
    print("Loading dataset...")
    df = pd.read_csv(csv_path)
    
    print(f"Dataset shape: {df.shape}")
    print(f"Categories found: {df['Category'].unique()}")
    print(f"\nCategory distribution:\n{df['Category'].value_counts()}\n")
    
    # Clean resume text
    print("Cleaning resume texts...")
    df['cleaned_resume'] = df['Resume'].apply(clean_resume_text)
    
    # Encode labels
    label_encoder = LabelEncoder()
    df['Category_encoded'] = label_encoder.fit_transform(df['Category'])
    
    return df['cleaned_resume'], df['Category_encoded'], label_encoder, df['Category']


def train_model(X, y):
    """
    Train the classification model.
    
    Args:
        X: Features (resume text)
        y: Labels (job categories)
        
    Returns:
        tuple: trained model, vectorizer, test metrics
    """
    print("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}\n")
    
    # Vectorize text using TF-IDF
    print("Vectorizing text using TF-IDF...")
    vectorizer = TfidfVectorizer(
        max_features=1500,
        min_df=2,
        max_df=0.8,
        stop_words='english',
        sublinear_tf=True
    )
    
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    print(f"TF-IDF feature shape: {X_train_tfidf.shape}\n")
    
    # Train Naive Bayes classifier
    print("Training Multinomial Naive Bayes classifier...")
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)
    
    # Make predictions
    print("Making predictions on test set...")
    y_pred = model.predict(X_test_tfidf)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n{'='*50}")
    print(f"Model Accuracy: {accuracy*100:.2f}%")
    print(f"{'='*50}\n")
    
    return model, vectorizer, X_test, y_test, y_pred


def save_model(model, vectorizer, label_encoder):
    """
    Save the trained model and preprocessing objects.
    
    Args:
        model: Trained classifier
        vectorizer: TF-IDF vectorizer
        label_encoder: Label encoder
    """
    print("Saving model and preprocessing objects...")
    
    # Save model
    with open('model/resume_classifier.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    # Save vectorizer
    with open('model/tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    
    # Save label encoder
    with open('model/label_encoder.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)
    
    print("✓ Model saved successfully to 'model/' directory\n")


def main():
    """Main training pipeline."""
    print("\n" + "="*50)
    print("Resume Screening Model Training")
    print("="*50 + "\n")
    
    # Load and prepare data
    X, y, label_encoder, categories = load_and_prepare_data('UpdatedResumeDataSet.csv')
    
    # Train model
    model, vectorizer, X_test, y_test, y_pred = train_model(X, y)
    
    # Print detailed classification report
    print("Classification Report:")
    print("="*50)
    target_names = label_encoder.classes_
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # Save model
    save_model(model, vectorizer, label_encoder)
    
    print("="*50)
    print("Training completed successfully!")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
