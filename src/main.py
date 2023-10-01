import structs
import utils
import os

from fpdf import FPDF
from datasets import load_dataset

pdf = FPDF()
squad_dataset = load_dataset('squad')

if __name__ == "__main__":
     if not os.path.exists("test"): os.mkdir("test", mode=0o666)
     
     utils.create_page(pdf, spacing=1)