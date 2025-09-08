#!/usr/bin/env python3
"""
Script to convert the populate_database.py file to PDF for submission
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import os

def convert_python_to_pdf():
    """Convert the Python script to PDF format."""
    
    # Read the Python file
    with open('populate_database.py', 'r', encoding='utf-8') as file:
        python_code = file.read()
    
    # Create PDF
    filename = "populate_database_submission.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Create custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=1,  # Center alignment
        textColor=colors.darkblue
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=8,
        leftIndent=20,
        rightIndent=20,
        spaceAfter=12,
        fontName='Courier'
    )
    
    # Build the PDF content
    story = []
    
    # Title
    title = Paragraph("Walmart Shipping Data Processing Script", title_style)
    story.append(title)
    story.append(Spacer(1, 20))
    
    # Description
    description = Paragraph(
        """
        <b>Task 4: Populate MySQL Database with Shipping Data</b><br/><br/>
        This script processes shipping data from three CSV files and populates a MySQL database 
        with products and shipments according to the existing schema.<br/><br/>
        
        <b>Data Structure:</b><br/>
        • shipping_data_0.csv: Self-contained shipping data<br/>
        • shipping_data_1.csv: Product data per shipment (multiple rows per shipment)<br/>
        • shipping_data_2.csv: Route data for shipments from shipping_data_1.csv<br/><br/>
        
        <b>Database Schema:</b><br/>
        • product table: id (INT AUTO_INCREMENT PRIMARY KEY), name (VARCHAR(255) NOT NULL)<br/>
        • shipment table: id (INT AUTO_INCREMENT PRIMARY KEY), product_id (INT NOT NULL), 
          quantity (INT NOT NULL), origin (VARCHAR(255)), destination (VARCHAR(255))<br/><br/>
        
        <b>Processing Results:</b><br/>
        • Total products: 45<br/>
        • Total shipments: 154<br/>
        • Total quantity: 5,908<br/>
        """,
        styles['Normal']
    )
    story.append(description)
    story.append(Spacer(1, 20))
    
    # Python code
    code_title = Paragraph("<b>Python Script:</b>", styles['Heading2'])
    story.append(code_title)
    story.append(Spacer(1, 12))
    
    # Add the Python code
    code_text = Preformatted(python_code, code_style)
    story.append(code_text)
    
    # Build PDF
    doc.build(story)
    
    print(f"PDF created successfully: {filename}")
    print(f"File size: {os.path.getsize(filename)} bytes")
    
    return filename

if __name__ == "__main__":
    try:
        pdf_file = convert_python_to_pdf()
        print(f"\n✓ Successfully created PDF: {pdf_file}")
        print("The PDF is ready for submission to the Walmart Forage task.")
    except Exception as e:
        print(f"Error creating PDF: {e}")
        print("Make sure you have reportlab installed: pip install reportlab")
