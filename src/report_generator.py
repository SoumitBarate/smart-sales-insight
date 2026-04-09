from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(kpis, insights, filename="report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Smart Sales Report", styles['Title']))
    content.append(Spacer(1, 10))

    content.append(Paragraph(f"Total Sales: {kpis['total_sales']}", styles['Normal']))
    content.append(Paragraph(f"Top Category: {kpis['top_category']}", styles['Normal']))
    content.append(Paragraph(f"Top Sub-Category: {kpis['top_sub_category']}", styles['Normal']))
    content.append(Paragraph(f"Top Region: {kpis['top_region']}", styles['Normal']))
    content.append(Paragraph(f"Top City: {kpis['top_city']}", styles['Normal']))

    content.append(Spacer(1, 10))
    content.append(Paragraph("AI Insights", styles['Heading2']))
    content.append(Paragraph(insights, styles['Normal']))

    doc.build(content)