# # # import tkinter as tk
# # # from tkinter import filedialog, messagebox
# # # import camelot

# # # def convert_pdf_to_csv():
# # #     file_path = filedialog.askopenfilename(
# # #         title="Select PDF File",
# # #         filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
# # #     )

# # #     if file_path:
# # #         try:
# # #             tables = camelot.read_pdf(file_path, pages="all")
# # #             for i, table in enumerate(tables):
# # #                 output_file = file_path.replace('.pdf', f'_table_{i + 1}.csv')
# # #                 table.to_csv(output_file)
# # #             messagebox.showinfo("Success", "PDF converted to CSV successfully!")
# # #         except Exception as e:
# # #             messagebox.showerror("Error", f"Failed to convert PDF: {e}")
# # #     else:
# # #         messagebox.showwarning("No File Selected", "Please select a valid PDF file.")

# # # root = tk.Tk()
# # # root.title("PDF to CSV Converter")
# # # root.geometry("400x200")

# # # btn = tk.Button(root, text="Select PDF and Convert to CSV", command=convert_pdf_to_csv)
# # # btn.pack(pady=50)

# # # root.mainloop()

# # import tkinter as tk
# # from tkinter import filedialog, messagebox
# # import camelot

# # def convert_pdf_to_csv():
# #     file_path = filedialog.askopenfilename(
# #         title="Select PDF File",
# #         filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
# #     )

# #     if file_path:
# #         try:
# #             tables = camelot.read_pdf(file_path, pages="all")
# #             for i, table in enumerate(tables):
# #                 output_file = file_path.replace('.pdf', f'_table_{i + 1}.csv')
# #                 table.to_csv(output_file)
# #             messagebox.showinfo("Success", "PDF converted to CSV successfully!")
# #         except Exception as e:
# #             messagebox.showerror("Error", f"Failed to convert PDF: {e}")
# #     else:
# #         messagebox.showwarning("No File Selected", "Please select a valid PDF file.")

# # root = tk.Tk()
# # root.title("PDF to CSV Converter")
# # root.geometry("400x200")

# # btn = tk.Button(root, text="Select PDF and Convert to CSV", command=convert_pdf_to_csv)
# # btn.pack(pady=50)

# # root.mainloop()


# # import tkinter as tk
# # from tkinter import filedialog, messagebox
# # import csv
# # import pdfplumber

# # def convert_pdf_to_csv():
# #     file_path = filedialog.askopenfilename(
# #         title="Select PDF File",
# #         filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
# #     )

# #     if file_path:
# #         try:
# #             with pdfplumber.open(file_path) as pdf:
# #                 for i, page in enumerate(pdf.pages):
# #                     table = page.extract_table()
# #                     if table:
# #                         output_file = file_path.replace('.pdf', f'_table_{i + 1}.csv')
# #                         with open(output_file, "w", newline="") as f:
# #                             writer = csv.writer(f)
# #                             writer.writerows(table)
# #             messagebox.showinfo("Success", "PDF converted to CSV successfully!")
# #         except Exception as e:
# #             messagebox.showerror("Error", f"Failed to convert PDF: {e}")
# #     else:
# #         messagebox.showwarning("No File Selected", "Please select a valid PDF file.")

# # root = tk.Tk()
# # root.title("PDF to CSV Converter")
# # root.geometry("400x200")

# # btn = tk.Button(root, text="Select PDF and Convert to CSV", command=convert_pdf_to_csv)
# # btn.pack(pady=50)

# # root.mainloop()



# # import tkinter as tk
# # from tkinter import filedialog, messagebox
# # import csv
# # import pdfplumber
# # import os

# # def convert_pdf_to_csv():
# #     file_path = filedialog.askopenfilename(
# #         title="Select PDF File",
# #         filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
# #     )

# #     if file_path:
# #         try:
# #             with pdfplumber.open(file_path) as pdf:
# #                 for i, page in enumerate(pdf.pages):
# #                     table = page.extract_table()
# #                     if table:
# #                         # Save CSV in the current directory
# #                         output_file = os.path.join(os.getcwd(), f'table_{i + 1}.csv')
# #                         with open(output_file, "w", newline="") as f:
# #                             writer = csv.writer(f)
# #                             writer.writerows(table)
# #                         print(f"Table {i + 1} saved as {output_file}")
# #             messagebox.showinfo("Success", "PDF converted to CSV successfully!")
# #         except Exception as e:
# #             messagebox.showerror("Error", f"Failed to convert PDF: {e}")
# #     else:
# #         messagebox.showwarning("No File Selected", "Please select a valid PDF file.")

# # root = tk.Tk()
# # root.title("PDF to CSV Converter")
# # root.geometry("400x200")

# # btn = tk.Button(root, text="Select PDF and Convert to CSV", command=convert_pdf_to_csv)
# # btn.pack(pady=50)

# # root.mainloop()
# import tkinter as tk
# from tkinter import filedialog, messagebox
# import csv
# import pdfplumber
# import os

# def convert_pdf_to_csv():
#     file_path = filedialog.askopenfilename(
#         title="Select PDF File",
#         filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
#     )

#     if file_path:
#         try:
#             with pdfplumber.open(file_path) as pdf:
#                 for i, page in enumerate(pdf.pages):
#                     table = page.extract_table()
#                     if table:
#                         # Save CSV in the current directory
#                         output_file = os.path.join(os.getcwd(), f'table_{i + 1}.csv')
#                         print(f"Extracted table {i + 1} from page {page.page_number}: {table[:5]}")  # Log first 5 rows
#                         print(f"Saving to: {output_file}")
#                         with open(output_file, "w", newline="") as f:
#                             writer = csv.writer(f)
#                             writer.writerows(table)
#                     else:
#                         print(f"No table found on page {page.page_number}")
#             messagebox.showinfo("Success", "PDF converted to CSV successfully!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to convert PDF: {e}")
#     else:
#         messagebox.showwarning("No File Selected", "Please select a valid PDF file.")

# root = tk.Tk()
# root.title("PDF to CSV Converter")
# root.geometry("400x200")

# btn = tk.Button(root, text="Select PDF and Convert to CSV", command=convert_pdf_to_csv)
# btn.pack(pady=50)

# root.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import pdfplumber
import os

def convert_pdf_to_csv():
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*"))
    )

    if file_path:
        try:
            output_file = os.path.join(os.getcwd(), f"{os.path.basename(file_path).replace('.pdf', '')}_output.csv")
            with pdfplumber.open(file_path) as pdf:
                with open(output_file, "w", newline="") as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(["SNo", "Name", "Symbol", "Date", "High", "Low", "Open", "Close", "Volume", "Marketcap"])  # Header row
                    for page in pdf.pages:
                        text = page.extract_text()
                        lines = text.split("\n")
                        for line in lines:
                            # Assuming rows are space-separated and have a fixed structure
                            if line.startswith("SNo") or line.strip() == "":
                                continue
                            data = line.split()  # Adjust this if data is not space-separated
                            if len(data) >= 10:  # Ensure all columns exist
                                writer.writerow(data[:10])
            messagebox.showinfo("Success", f"PDF converted to CSV successfully! Saved at {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert PDF: {e}")
    else:
        messagebox.showwarning("No File Selected", "Please select a valid PDF file.")

root = tk.Tk()
root.title("PDF to CSV Converter")
root.geometry("400x200")

btn = tk.Button(root, text="Select PDF and Convert to CSV", command=convert_pdf_to_csv)
btn.pack(pady=50)

root.mainloop()
