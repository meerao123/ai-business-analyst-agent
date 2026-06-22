from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

def generate_insights(results):
    prompt = f"""
    You are an experienced business analyst.

    Analyze the following sales metrics:

    Total Sales: {results['total_sales']}
    Average Sales: {results['avg_sales']}
    Best Month: {results['best_month']}
    Worst Month: {results['worst_month']}

    Provide:
    1. Key insights
    2. Possible reasons for the trends
    3. Actionable recommendations

    Keep the response concise and professional.
    """
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
    )
        return response.text

    except Exception as e:
        return f"Error: {e}"

