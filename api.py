from fastapi import FastAPI
from analysis import analyze_sales

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Working"}

@app.get("/analyze")
def analyze():

    results = analyze_sales("sales.csv")

    return results