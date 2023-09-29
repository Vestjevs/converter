from fpdf import FPDF
from datasets import load_dataset

# TODO: create special dict for parsed data

pdf = FPDF()
squad_dataset = load_dataset('squad')

new_line = lambda x, h: x.write(h, txt="\n")
code_line = lambda x, h: x.write(h, txt= (10 * "~" + "\n"))

N_TABS = 4
FILE_NAME = "test_file"

def add_author_data(data : str) -> None:
    author = "Username"
    create_date = "02.02.02"
    change_date = "03.03.03"
    pdf.write(3, txt=f"Author: {author}")
    new_line(pdf, 3)
    pdf.write(3, txt=f"Creation date: {create_date}")
    new_line(pdf, 3)
    pdf.write(3, txt=f"Changing date: {change_date}")


def add_code(txt_code: str) -> None:
    code_line(pdf, 3)
    
    pdf.write(3, txt="def hello_word():\n")
    pdf.write(3, txt= N_TABS * " " + "print(\"Hello from test world\")")
    
    new_line(pdf, 3)
    code_line(pdf, 3)


def create_page(spacing=1) -> None:
    pdf.add_page()
    
    pdf.set_font("Arial", size=7)
    context = str(squad_dataset['train'][0]['context']).split('.')
    
    add_author_data("")
    
    new_line(pdf, 5)
    add_code("")    
    pdf.output(f"test/{FILE_NAME}.pdf")

if __name__ == "__main__":
    create_page()