
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.image("ali.jpg", x=10, y=10, w=200)
pdf.set_font("Arial", size=12)
pdf.ln(60)
pdf.cell(200, 10, txt="", ln=True, align="C")
pdf.output("img_to_pdf.pdf")
print("PDF created successfully!")
# print("Please check the current directory for the file 'img_to_pdf.pdf'")
print("img_to_pdf.pdf")