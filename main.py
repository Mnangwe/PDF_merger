import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()


for file in os.listdir():
    if file.endswith('.pdf'):
        merger.append(file)
    merger.write("merged/combinedDocs.pdf")