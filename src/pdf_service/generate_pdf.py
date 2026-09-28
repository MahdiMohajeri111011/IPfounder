from reportlab.pdfgen import canvas


def create_pdf(data):
    pdf = canvas.Canvas("result.pdf")
    pdf.drawString(100, 750, f"IP: {data['ip']}")
    pdf.drawString(100, 730, f"Type: {data['type']}")
    pdf.drawString(100, 710, f"Country: {data['country_name']}")
    pdf.drawString(100, 690, f"Region: {data['region_name']}")
    pdf.drawString(100, 670, f"City: {data['city']}")
    pdf.drawString(100, 650, f"ZIP: {data['zip']}")
    pdf.drawString(100, 630, f"Latitude: {data['latitude']}")
    pdf.drawString(100, 610, f"Longitude: {data['longitude']}")

    pdf.save()