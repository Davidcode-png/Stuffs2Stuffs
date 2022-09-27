import os
from django.shortcuts import render,HttpResponse
from .forms import FileForm
from .utils import pdftoword, wordtopdf
from docx2pdf import convert
import time

def pdftodocx(request):
    form  = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            file = form.save()
            document,path = pdftoword(file)
            
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename = "{form.name}.docx"'
            document.save(response)
            return response
                    
    context = {'form':form}

    return render(request,'convertapp/index.html',context)


def docxtopdf(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save()
            pdf = wordtopdf(file_instance)
            
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=download.pdf'
            return response
            

    
    context = {'form':form}
    
    return render(request, 'convertapp/index.html',context)

