import structs

new_line = lambda x, h: x.write(h, txt="\n")

code_line = lambda x, h: x.write(h, txt= (10 * "~" + "\n"))

def make_struct_author() -> None:
    return structs.author(name="Foo", create_date="02/02/02", change_date="03/03/03")

def add_author_data(pdf, author: structs.author) -> None:
    pdf.write(3, txt=f"Author: {author.name}")
    new_line(pdf, 3)
    pdf.write(3, txt=f"Creation date: {author.create_date}")
    new_line(pdf, 3)
    pdf.write(3, txt=f"Changing date: {author.change_date}")


def add_code(pdf, txt_code: str) -> None:
    code_line(pdf, 3)
    
    pdf.write(3, txt="def hello_word():\n")
    pdf.write(3, txt=structs.N_TABS * " " + "print(\"Hello from test world\")")
    
    new_line(pdf, 3)
    code_line(pdf, 3)


def create_page(pdf, spacing=1) -> None:
    pdf.add_page()
    
    pdf.set_font("Arial", size=7)
    # context = str(squad_dataset['train'][0]['context']).split('.')
    
    add_author_data(make_struct_author())
    
    new_line(pdf, 5)
    add_code("")
    
    pdf.output(f"test/{structs.FILE_NAME}.pdf")