import pandas as pd
import plotly.express as px 

def create_chart(file_path):

    df = pd.read_csv(file_path)

    bar_chart = px.bar(
        df,
        x="Month",
        y="Sales",
        title="monthly sales comparisn"
    )

    bar_chart.write_html("bar_chart.html")

    line_chart = px.line(
        df,
        x="Month",
        y="Sales",
        title="Monthly Sales Trend"
    )

    line_chart.write_html("line_chart.html")