from fpdf import FPDF
from datasets import load_dataset

# TODO: create special dict for parsed data

pdf = FPDF()
squad_dataset = load_dataset('squad')

def create_page(spacing=1):
    pdf.add_page()

    pdf.set_font("Arial", size=7)
    context = str(squad_dataset['train'][0]['context']).split('.')
    
    pdf.cell(2)
    for id, line in enumerate(context):
        line = line + "."
        pdf.write(5, txt=line)

    file_name = "test_file"
    pdf.output(f"test/{file_name}.pdf")

if __name__ == "__main__":
    create_page()