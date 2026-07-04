from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_insights(results):

    prompt = f"""
    You are an experienced business analyst.

Analyze the following sales metrics:

Total Sales: 57000
Average Sales: 11400
Best Month: Apr
Worst Month: Mar

Provide:
1. Key insights
2. Possible reasons for the trends
3. Actionable recommendations
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"