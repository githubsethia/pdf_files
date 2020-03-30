#Below code demonstrates how to read file, rotate the page clockwise and 
#write to another file

import PyPDF2

with open('original.pdf','rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    pg = reader.getPage(0)
    pg.rotateClockwise(90)
    print(type(pg))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(pg)
    with open('tilt.pdf','wb') as file2:
        file2 = writer.write(file2)
