# March 19, 2021
# Sandra Milena Lopez Zamora
# slopezza@outlook.com
# Tutorial: https://towardsdatascience.com/how-to-properly-ship-and-deploy-your-machine-learning-model-8a8664b763c4

from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

class PredictRequest(BaseModel):
    data: List[List[float]]

class PredictResponse(BaseModel):
    data: List[float]


app = FastAPI()

@app.post("/predict", response_model=PredictResponse)
def predict(input: PredictRequest):
    return PredictResponse(data=[0, 0])
