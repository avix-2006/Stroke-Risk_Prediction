# report.py
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from datetime import datetime

# CHANGE: Change output_path to response_stream (accepts BytesIO buffer)
def generate_report(image_path, prediction, prob, intensity, contrast, edge_density, response_stream):

    # Pass the stream buffer directly into SimpleDocTemplate
    doc = SimpleDocTemplate(response_stream, pagesize=A4)

    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("🏥 HOSPITAL DIAGNOSTIC REPORT", styles["Title"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph("NeuroVision AI - Stroke Risk Analysis System", styles["Normal"]))
    content.append(Spacer(1, 12))

    content.append(Paragraph(
        f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        styles["Normal"]
    ))
    content.append(Spacer(1, 20))

    try:
        content.append(Image(image_path, width=200, height=200))
        content.append(Spacer(1, 15))
    except:
        pass

    data = [
        ["Parameter", "Value"],
        ["Prediction", prediction],
        ["Stroke Risk (%)", prob],
        ["Intensity", intensity],
        ["Contrast", contrast],
        ["Edge Density", edge_density]
    ]

    table = Table(data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))

    content.append(table)
    content.append(Spacer(1, 20))

    if prob < 30:
        msg = "Low risk detected."
    elif prob < 70:
        msg = "Moderate risk detected."
    else:
        msg = "High risk detected."

    content.append(Paragraph(msg, styles["Normal"]))

    doc.build(content)

    return response_stream  # Return the filled buffer