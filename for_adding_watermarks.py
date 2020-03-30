import PyPDF2

#add watermark to all the pdf files
read_f1 = PyPDF2.PdfFileReader(open('merged_pdf.pdf','rb'))
read_f2 = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
#Create a writer object
writer = PyPDF2.PdfFileWriter()
#add the page from file 1
for page in range(read_f1.getNumPages()):
    page_content = read_f1.getPage(page)
    #merge the watermark from file 2
    page_content.mergePage(read_f2.getPage(0))
    #add to writer object
    writer.addPage(page_content)

with open('watermarked_merged.pdf','wb') as file:
    writer.write(file)



