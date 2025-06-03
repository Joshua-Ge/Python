from fpdf import FPDF

def txt_to_pdf(txt_file_path, pdf_file_path):
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Open and read the text file
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Replace problematic characters if necessary
            line = line.replace("’", "'").replace("“", '"').replace("”", '"')
            pdf.multi_cell(0, 10, line.strip())

    # Output the PDF
    pdf.output(pdf_file_path)
    print(f"PDF saved as: {pdf_file_path}")

# Example usage
txt_file = "example.txt"
pdf_file = "example_output.pdf"
txt_to_pdf(txt_file, pdf_file)