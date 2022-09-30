import os
from django.shortcuts import HttpResponse
from docx import Document
from pdf2docx import Converter
from docx2pdf import convert
import time
import fitz
from PIL import Image
import img2pdf

def helper_pdftoword(file_instance):
    try:
        file_path = file_instance.file.path
    except:
        file_path = os.path.abspath(file_instance) 
    file_dir = os.path.dirname(file_path)
    file = open(file_path)
    cv = Converter(file)
    cv.convert(f'{file_dir}\OutputTest2.docx')

    cv.close()
    document = Document(f'{file_dir}\OutputTest2.docx')
    return document,file_path

    
def helper_wordtopdf(file_instance):
    file_path = file_instance.file.path
    file_dir = os.path.dirname(file_path)
    
    convert(file_path,f'{file_dir}/{file_instance.name}.pdf')
    pdf_instance = f'{file_dir}/{file_instance.name}.pdf'
    
    time.sleep(1) # Prevents threading issues 'Error CoInitialize has not been called'
    
    pdf = open(pdf_instance,'rb')
    print(os.path.abspath(pdf_instance))
    print()
    print()
    return pdf,pdf_instance


def helper_pdftojpg(file_instance):

    # Checks if the file has been converted , in that case
    # it returns a string instead of the file instance
    try:
        file_path = file_instance.file.path
    except:
        file_path = os.path.abspath(file_instance) 
        
    input_pdf = file_path
    file_dir = os.path.dirname(file_path)
    output_name = f"{file_dir}/output.tiff"

    zoom = 0.9 # to increase/decrease the resolution
    mat = fitz.Matrix(zoom, zoom)

    doc = fitz.open(input_pdf)
    image_list = []
    for page in doc:
        pix = page.get_pixmap(matrix = mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        image_list.append(img)


    if image_list:
        image_list[0].save(
            output_name,
            save_all=True,
            append_images=image_list[1:],
            # compression=compression,
            dpi=(100, 100),
        )
    
    x = open(output_name,"rb")

    return x


def helper_imgtopdf(file_instance):
    try:
        file_path = file_instance.file.path
    except:
        file_path = os.path.abspath(file_instance) 
    file_dir = os.path.dirname(file_path)
    pdf_path = f"{file_dir}/Output.pdf"
    # opening image
    image = Image.open(file_path)

    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)

    # opening or creating pdf file
    file = open(pdf_path, "wb")

    # writing pdf files with chunks
    file.write(pdf_bytes)

    # closing image file
    image.close()

    new_file = open(pdf_path,"rb")

    return new_file,pdf_path


def helper_check_file_extension(file_instance,extension):
    if file_instance.extension != extension:
        return HttpResponse("Invalid File Extension")