import sys
import os
import PyPDF2
from pathlib import Path

# Getting PDF file information

downloadFolder = str(os.path.join(Path.home(), "Downloads"))
os.chdir(downloadFolder)
writer = PyPDF2.PdfFileWriter()


while (True):
    name = input("Input PDF file to add: ")
    if name == "":
        break
    filePath = os.path.abspath(name)

    # Making sure path exists
    if not os.path.exists(filePath):
        print("File not found")
        sys.exit()

    # Setting up variables for PDF file
    pdfFile = open(filePath, "rb")
    reader = PyPDF2.PdfFileReader(pdfFile)
    pages = reader.numPages
    for n in range(pages):
        page = reader.getPage(n)
        writer.addPage(page)

fileName = input("Input name of combined PDF: ")
outputFile = open(fileName, "wb")
writer.write(outputFile)
outputFile.close()
pdfFile.close()