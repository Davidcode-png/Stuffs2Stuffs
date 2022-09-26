import os
from django.shortcuts import HttpResponse
from docx import Document
from pdf2docx import Converter

def pdftoword(form):
    file_path = form.file.path
    file_dir = os.path.dirname(file_path)
    file = open(form.file.path)
    cv = Converter(file)
    cv.convert(f'{file_dir}\OutputTest2.docx')

    cv.close()
    document = Document(f'{file_dir}\OutputTest2.docx')
    return document,file_path
    