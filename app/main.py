# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 11:25:48 2023

@author: sbhadwal
"""

import pandas as pd
from pycaret.classification import *
from fastapi import FastAPI
import uvicorn

import nest_asyncio
nest_asyncio.apply()

app = FastAPI()
model = load_model('./deployment_28042020')

@app.post('/predict')

def predict(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    data = pd.DataFrame([[CreditScore, Geography, Gender, Age, Tenure, Balance, 
                          NumOfProducts, HasCrCard, 
                          IsActiveMember, EstimatedSalary]])
    
    data.columns = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 
                    'NumOfProducts', 'HasCrCard', 
                    'IsActiveMember', 'EstimatedSalary']

    predictions = predict_model(model, data=data) 
    return {'prediction': int(predictions['Label'][0])}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)