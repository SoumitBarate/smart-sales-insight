import streamlit as st
from src.analysis import load_data, clean_data, generate_kpis
from src.claude_api import generate_insights
from src.report_generator import create_pdf

st.title("📊 Smart Sales Insight Generator")

# Upload file
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:

    # Load & clean
    df = load_data(uploaded_file)
    df = clean_data(df)

    st.subheader("📄 Data Preview")
    st.dataframe(df.head())

    # Generate KPIs
    kpis = generate_kpis(df)

    st.subheader("📊 KPIs")
    st.metric("Total Sales", kpis['total_sales'])
    st.write("Top Category:", kpis['top_category'])
    st.write("Top Sub-Category:", kpis['top_sub_category'])
    st.write("Top Region:", kpis['top_region'])
    st.write("Top City:", kpis['top_city'])

    # Chart
    st.subheader("📈 Monthly Sales Trend")
    monthly_chart = df.groupby('Order Date')['Sales'].sum()
    st.line_chart(monthly_chart)

    # AI Insights
    if st.button("Generate Insights 🤖"):
        insights = generate_insights(kpis)

        st.subheader("🧠 AI Insights")
        st.write(insights)

        # Generate PDF
        create_pdf(kpis, insights)

        with open("report.pdf", "rb") as f:
            st.download_button("Download Report", f, "sales_report.pdf")