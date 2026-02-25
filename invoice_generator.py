from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os

def generate_invoice(items, filename="invoice.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Invoice")
    c.setFont("Helvetica", 12)
    
    y = height - 100
    line_height = 20
    total = 0
    
    for idx, item in enumerate(items):
        line = f"{item['name']} | Qty: {item['qty']} | Price: {item['price']} | Subtotal: {item['qty']*item['price']}"
        c.drawString(50, y, line)
        total += item['qty'] * item['price']
        y -= line_height
        
        # Check if y is too low for next line → add new page
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 12)
            y = height - 50
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y - 10, f"Total: {total}")
    c.save()
    
    return os.path.abspath(filename)