import creator
import os
import structs
import test_code_parser

from fpdf import FPDF
from datasets import load_dataset

pdf = FPDF()
squad_dataset = load_dataset('squad')

if __name__ == "__main__":
     if not os.path.exists(f"{structs.DIR_OUTPUT}"): os.mkdir(f"{structs.DIR_OUTPUT}", mode=0o666)
     
     test_code_parser.test_parse_cpp_func_intro()
     