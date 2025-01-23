import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
from src.pipeline.predict_pipeline import predict as predict_price

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/",response_class=HTMLResponse)
def serve_homepage():
    file_path = os.path.join(os.getcwd(), "static", "index.html")
    with open(file_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content) 
class Features(BaseModel):
    income: float
    house_age: float
    num_rooms: float
    num_bedrooms: float
    population: float
    address: str