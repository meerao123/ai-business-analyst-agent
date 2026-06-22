from analysis import analyze_sales 
from charts import create_chart
from ai_insights import generate_insights

create_chart("sales.csv")
result=analyze_sales("sales.csv")
insights=generate_insights(result)
print(insights)