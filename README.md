# Airline-Sentiment-Analysis

## Overview
This project implements an Airline Sentiment Analysis system using natural language processing (NLP) techniques with the SpaCy library. The model classifies airline-related comments as either positive or negative based on the sentiment expressed in the text. The dataset used for this analysis is sourced from airline sentiment analysis data.

## Features
- **Data Preprocessing**: Cleans the dataset by removing unnecessary tags, links, and hashtags.
- **Balanced Dataset**: Ensures an equal representation of positive and negative sentiments.
- **Model Training**: Utilizes SpaCy's transformer-based architecture for training a sentiment classification model.
- **Binary Document Conversion**: Converts the dataset into binary format suitable for SpaCy training.
- **Model Evaluation**: Tests the trained model on new input texts to predict sentiment.

## Requirements
To run this project, you need the following libraries:
- `pandas`
- `spacy`
- `spacy-transformers`
- `numpy`
- `matplotlib` (optional, for visualization)

You can install the required libraries using pip:
```code
pip install pandas spacy spacy-transformers numpy matplotlib
```
Additionally, download the SpaCy English transformer model:
```code
python -m spacy download en_core_web_trf
```

## Dataset
The dataset used in this project is a CSV file containing airline comments and their corresponding sentiments. The dataset should be structured with at least two columns:
- `airline_sentiment`: Contains the sentiment label (positive or negative).
- `text`: Contains the comment text.

## Usage
- After cloning the repo, run
```code
python app.py
```
- Open the localhost link, route to /predict and type in your Airline Experience.
- Model will analyse and decode your rating into positive or negative experience.

## Conclusion
This project serves as a robust foundation for performing sentiment analysis on airline-related comments using advanced NLP techniques.

