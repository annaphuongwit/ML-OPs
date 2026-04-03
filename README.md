# Customer Feedback Analysis

To run the project, install dependencies and run the main script.

# Sentiment Analysis Project

## Setup

### Option 1: Python venv
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

### Option 2: Conda
conda create -n sentiment-env python=3.11 -y
conda activate sentiment-env
pip install -r requirements.txt

## Train
python src/train.py --data data/train.csv --out models/sentiment.joblib

# ML-OPs
Chaotic workflows lead to lost functions, confusing scripts, and “it works on my machine” errors that block collaboration and reproducibility. This project teaches you to replace error-prone methods with a professional automated workflow, culminating in a complete CI/CD pipeline for reliable, sharable code. Final of Project: Code Push,Automated Checks,Quality Gate: The pipeline has a built-in safety check. It will only proceed if both the tests and,Automated Build,Publish

