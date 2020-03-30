
# Need to give python file name followed by name of pdf files to be merged_pdf
# example:python pdf.py original.pdf twopage.pdf

import PyPDF2
import sys

#Merge multiple PDF files
inputs = sys.argv[1:]
print(inputs)

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for file in pdf_list:
        merger.append(file)
    merger.write('merged_pdf.pdf')
        
pdf_merger(inputs)
