import requests
import os

def generate_insights(kpis):

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        return "❌ API key not found."

    prompt = f"""
    You are a data analyst.

    Analyze this sales data:

    Total Sales: {kpis['total_sales']}
    Top Category: {kpis['top_category']}
    Top Sub-Category: {kpis['top_sub_category']}
    Top Region: {kpis['top_region']}
    Top City: {kpis['top_city']}

    Monthly Sales Trend:
    {kpis['monthly_sales']}

    Segment-wise Sales:
    {kpis['segment_sales']}

    Give:
    - Key Insights
    - Business Recommendations
    - Growth Opportunities
    """

    try:
        # 🔥 THIS IS WHERE YOUR CODE GOES
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost",
                "X-Title": "Sales Insight App"
            },
            json={
                "model": "meta-llama/llama-3-8b-instruct",
                "messages": [{"role": "user", "content": prompt}]
            }
        )

        data = response.json()
        print("DEBUG RESPONSE:", data)

        if "choices" in data:
            return data['choices'][0]['message']['content']
        elif "error" in data:
            return f"❌ API Error: {data['error']['message']}"
        else:
            return "❌ Unexpected API response"

    except Exception as e:
        return f"❌ Exception: {str(e)}"