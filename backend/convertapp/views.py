from django.shortcuts import render,HttpResponse
from .forms import FileForm
from .models import File
from pdf2docx import Converter
import os
from django.conf import settings
import img2pdf
from docx import Document
from .utils import pdftoword

def index(request):
    form  = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form = form.save()
            document,path = pdftoword(form)
            
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename = "{form.name}.docx"'
            document.save(response)
            return response
                    
    context = {'form':form}
    # if request.method == 'POST':
    #     pdf = request.FILES['pdf']
    #     cv = Converter(pdf)
    #     test = cv.convert('Output.docx')

    #     return HttpResponse(test,content_type='application/docx')
        

    return render(request,'convertapp/index.html',context)

def imgtopdf(request):
    if request.method == 'POST':
        img = request.FILES['pdf']
        cv = Converter(img)
        test = cv.convert('Output.docx')
        cv.close()

        return HttpResponse(test, content_type='application/docx')
    return render(request, 'convertapp/imgtopdf.html')