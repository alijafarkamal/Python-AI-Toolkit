# from pdfminer.high_level import extract_text

# # Extract text from a PDF file
# file_path = "lec2.pdf"  # Replace with your PDF file path
# text = extract_text(file_path)

# # Save the extracted text to a .txt file
# with open("output.txt", "w") as f:
#     f.write(text)


# from pdf2image import convert_from_path

# # Convert PDF to images
# file_path = "Transcript.pdf"  # Replace with your PDF file path
# images = convert_from_path(file_path)

# # Save each page as an image
# for i, image in enumerate(images):
#     image.save(f"page_{i + 1}.png", "PNG")




# import csv
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas

# # Load your CSV file
# csv_file = "coin_Dogecoin.csv"  # Replace with your CSV file path
# pdf_file = "coin_Dogecoin1.pdf"   # Output PDF file name

# # Create PDF
# c = canvas.Canvas(pdf_file, pagesize=letter)
# width, height = letter
# y = height - 40  # Start height for text

# # Open the CSV file
# with open(csv_file, "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         text = "  ".join(row)  # Join CSV values with spaces for formatting
#         c.drawString(40, y, text)  # Add text to the PDF
#         y -= 20  # Move to the next line
#         if y < 40:  # Add a new page if space runs out
#             c.showPage()
#             y = height - 40

# # Save the PDF
# c.save()
# print(f"CSV converted to PDF and saved as '{pdf_file}'")


# import csv
# from fpdf import FPDF

# # Load your CSV file
# csv_file = "coin_Dogecoin.csv"  # Replace with your CSV file path
# pdf_file = "coin_Dogecoin.pdf"    # Output PDF file name

# # Initialize FPDF
# pdf = FPDF()
# pdf.set_auto_page_break(auto=True, margin=15)
# pdf.add_page()
# pdf.set_font("Arial", size=12)

# # Open the CSV file
# with open(csv_file, "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         line = "  ".join(row)  # Join CSV values with spaces for formatting
#         pdf.cell(0, 10, txt=line, ln=True)  # Add each line to the PDF

# # Save the PDF
# pdf.output(pdf_file)
# print(f"CSV converted to PDF and saved as '{pdf_file}'")



import camelot

# Load the PDF and extract tables
file_path = "coin_Dogecoin1.pdf"  # Replace with your PDF file path
tables = camelot.read_pdf(file_path, pages="all")

# Save tables as CSV
for i, table in enumerate(tables):
    table.to_csv(f"table_{i + 1}.csv")
    print(f"Table {i + 1} saved as 'table_{i + 1}.csv'")
