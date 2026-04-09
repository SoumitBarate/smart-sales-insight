import pandas as pd

def load_data(file):
    return pd.read_csv(file)

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    # Convert date
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

    return df

def generate_kpis(df):

    total_sales = df['Sales'].sum()

    top_category = df.groupby('Category')['Sales'].sum().idxmax()
    top_sub_category = df.groupby('Sub-Category')['Sales'].sum().idxmax()
    top_region = df.groupby('Region')['Sales'].sum().idxmax()
    top_city = df.groupby('City')['Sales'].sum().idxmax()

    monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
    segment_sales = df.groupby('Segment')['Sales'].sum()

    return {
        "total_sales": round(total_sales, 2),
        "top_category": top_category,
        "top_sub_category": top_sub_category,
        "top_region": top_region,
        "top_city": top_city,
        "monthly_sales": monthly_sales.to_string(),
        "segment_sales": segment_sales.to_string()
    }