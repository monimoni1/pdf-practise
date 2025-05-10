import PyPDF2
import sys

watermark = "wtr.pdf"
specimen = "super.pdf"

def watermark_maker(watermark_specimen, pdf_specimen):
    for logo in watermark_specimen:
        watermark = PyPDF2.PdfFileReader(logo, 'rb')
    for pdf in pdf_specimen:
        reader = PyPDF2.PdfFileReader(pdf, 'rb')
        page = reader.pages[0]

    page.mergePage(watermark.pages[0])
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open("Watermarked.pdf", 'wb') as file:
        output.write(file)


watermark_maker(watermark, specimen)



