import os
import subprocess
import PyPDF2

def ppttopdf(input_path):
    def powerpoint_to_pdf(input_file_path, output_file_path):
        subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', input_file_path])
        os.rename(f'{os.path.splitext(input_file_path)[0]}.pdf', output_file_path)

    def merge_pdfs(pdf_list, output_path):
        pdf_merger = PyPDF2.PdfMerger()
        for pdf in pdf_list:
            with open(pdf, 'rb') as f:
                pdf_merger.append(PyPDF2.PdfFileReader(f))
        with open(output_path, 'wb') as f:
            pdf_merger.write(f)

    # Specify input and output file paths
    input_file_path = input_path
    output_file_path = 'tt.pdf'

    # Convert PowerPoint file to PDF
    powerpoint_to_pdf(input_file_path, output_file_path)
