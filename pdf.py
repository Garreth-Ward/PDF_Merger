import PyPDF2
import sys

inputs = sys.argv[1:]


#Merges PDF's given as arugments in cmd line
#Command to run: python .\pdf.py .\dummy.pdf .\tilt.pdf .\twopage.pdfdef pdf_merger(pdf_lists):
def pdf_merger(pdf_lists):
    try:
        # Combine PDFs
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_lists:
            merger.append(pdf)
        merger.write('super.pdf')

        # Explicitly close the merger object
        merger.close()

        # Check if the user wants to watermark
        will_watermark = input("Do you want to watermark? Enter y/n: ")
        if will_watermark == 'y':
            pdf_watermark('super.pdf', 'wtr.pdf', 'watermarked_page.pdf')

        else:
            print("Files merged but not watermarked")

    except Exception as e:
        print(f"An error occurred: {e}")


def pdf_watermark(input_pdf, watermark_pdf, output_pdf):
    try:
        template = PyPDF2.PdfFileReader(open(input_pdf, 'rb'))
        watermark = PyPDF2.PdfFileReader(open(watermark_pdf, 'rb'))
        output = PyPDF2.PdfFileWriter()

        for i in range(template.getNumPages()):
            page = template.getPage(i)
            page.mergePage(watermark.getPage(0))
            output.addPage(page)

        with open(output_pdf, 'wb') as file:
            output.write(file)
            print("File Watermarked")

    except Exception as e:
        print(f"An error occurred: {e}")


pdf_merger(inputs)


