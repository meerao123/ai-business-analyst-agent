
import pandas as pd

def analyze_sales(file_path):
    df=pd.read_csv(file_path)

    total_sales=df["Sales"].sum()
    avg_sales=df["Sales"].mean()

    max_sales=df["Sales"].max()
    best_month=df[df["Sales"]==max_sales]["Month"].iloc[0]

    min_sales=df["Sales"].min()
    worst_month=df[df["Sales"]==min_sales]["Month"].iloc[0]
    
    return {
    "total_sales": int(total_sales),
    "avg_sales": float(avg_sales),
    "best_month": str(best_month),
    "worst_month": str(worst_month)
}