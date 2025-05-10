import PyPDF2
import sys

watermark_file = sys.argv[1]
input_file = sys.argv[2]

def watermark_maker(watermark_file, pdf_file):
    with open(watermark_file, 'rb') as wtr_file:
        watermark = PyPDF2.PdfFileReader(wtr_file)
        watermark_page = watermark.getPage(0)

    with open(pdf_file, 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        writer = PyPDF2.PdfFileWriter()

        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            page.mergePage(watermark_page)
            writer.addPage(page)


with open("watermarked.pdf", 'wb') as output_files:
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(output_files)

