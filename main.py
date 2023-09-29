from fpdf import FPDF
from datasets import load_dataset

# TODO: create special dict for parsed data

pdf = FPDF()
squad_dataset = load_dataset('squad')

new_line = lambda x, indent: x.write(indent, txt="\n")
N_TABS = 4

def create_page(spacing=1):
    pdf.add_page()
    
    pdf.set_font("Arial", size=7)
    context = str(squad_dataset['train'][0]['context']).split('.')
    
    author = "Username"
    create_date = "02.02.02"
    change_date = "03.03.03"
    pdf.write(3, txt=f"Author: {author}")
    new_line(pdf, 3)
    pdf.write(3, txt=f"Creation date: {create_date}")
    new_line(pdf, 3)
    pdf.write(3, txt=f"Changing date: {change_date}")
    
    new_line(pdf, 5)
    
    pdf.write(3, txt="def hello_word():\n")
    pdf.write(3, txt= N_TABS * " " + "print(\"Hello from test world\")")
    
    file_name = "test_file"
    pdf.output(f"test/{file_name}.pdf")

if __name__ == "__main__":
    create_page()