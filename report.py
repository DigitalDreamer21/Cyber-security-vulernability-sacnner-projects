from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(results, filename="report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Cybersecurity Scan Report", styles['Title']))

    for line in results:
        content.append(Paragraph(line, styles['Normal']))

    doc.build(content)