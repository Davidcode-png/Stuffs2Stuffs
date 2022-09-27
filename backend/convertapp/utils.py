import os
from django.shortcuts import HttpResponse
from docx import Document
from pdf2docx import Converter
from docx2pdf import convert
import time


def pdftoword(form):
    file_path = form.file.path
    file_dir = os.path.dirname(file_path)
    file = open(form.file.path)
    cv = Converter(file)
    cv.convert(f'{file_dir}\OutputTest2.docx')

    cv.close()
    document = Document(f'{file_dir}\OutputTest2.docx')
    return document,file_path
    
def wordtopdf(file_instance):
    file_path = file_instance.file.path
    file_dir = os.path.dirname(file_path)
    
    convert(file_path,f'{file_dir}/{file_instance.name}.pdf')
    pdf_instance = f'{file_dir}/{file_instance.name}.pdf'
    
    time.sleep(1) # Prevents threading issues 'Error CoInitialize has not been called'
    
    pdf = open(pdf_instance,'rb')

    return pdf