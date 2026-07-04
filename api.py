from fastapi import FastAPI
from analysis import analyze_sales
from ai_insights import generate_insights

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Working"}

@app.get("/analyze")
def analyze():

    results = analyze_sales("sales.csv")
    insights=generate_insights(results)

    return {
        "analysis":results,
        "ai_insights":insights
    }