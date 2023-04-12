import os
import comtypes.client
import PyPDF2

def ppttopdf():
    def powerpoint_to_pdf(input_file_path, output_file_path):
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        powerpoint.Visible = 1
        slides = powerpoint.Presentations.Open(input_file_path)
        slides.SaveAs(output_file_path, FileFormat=32)  # 32 for pdf
        slides.Close()
        powerpoint.Quit()

    def merge_pdfs(pdf_list, output_path):
        pdf_merger = PyPDF2.PdfMerger()
        for pdf in pdf_list:
            with open(pdf, 'rb') as f:
                pdf_merger.append(PyPDF2.PdfFileReader(f))
        with open(output_path, 'wb') as f:
            pdf_merger.write(f)

    # Specify input and output file paths
    input_file_path = r'C:\Users\user\Desktop\python\tt.ppt'
    output_file_path = r'C:\Users\user\Desktop\python\tt.pdf'

    # Convert PowerPoint file to PDF
    powerpoint_to_pdf(input_file_path, output_file_path)
