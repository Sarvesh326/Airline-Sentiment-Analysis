# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:32:51 2022

@author: user
"""

# 1. Library imports
#pip install fastapi uvicorn
import uvicorn
from fastapi import FastAPI
from reviews import Review

import spacy
# 2. Create the app object
app = FastAPI()

# Loading the best model from output_updated folder
nlp = spacy.load("output_updated/model-best") # Update Path

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {f'Welcome {name} sir!! Thank you for this opportunity.'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_sentiment(data:Review):
    data = data.dict()
    text=data['text']
    
    demo = nlp(text)
    sent = demo.cats
    prediction = max(sent, key=sent.get)
    
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload