import os
from django.shortcuts import render,HttpResponse
from .forms import FileForm
from .models import File
from .utils import helper_imgtopdf, helper_pdftoword,helper_pdftojpg ,helper_wordtopdf


def index(request):
    File.objects.all().delete()
    return render(request,'convertapp/home.html')

def pdftodocx(request):
    source = 'PDF'
    converted = 'Word'
    form  = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.save()
            if file.extension != '.pdf':
                return render(request,'convertapp/errorfiletype.html')
            document,path = helper_pdftoword(file)
            
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename = "Output.docx"'
            document.save(response)
            return response
                    
    context = {'form':form,'source':source,'converted':converted}

    return render(request,'convertapp/index.html',context)


def docxtopdf(request):
    source = 'Word'
    converted = 'PDF'
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save()
            if file_instance.extension != '.docx':
                return render(request,'convertapp/errorfiletype.html')

            pdf,pdf_path = helper_wordtopdf(file_instance)
            
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=download.pdf'
            return response
            

    
    context = {'form':form,'source':source,'converted':converted}
    
    return render(request, 'convertapp/index.html',context)



def pdftojpg(request):
    source = 'PDF'
    converted = 'Image'
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save()
            if file_instance.extension != '.pdf':
                return render(request,'convertapp/errorfiletype.html')

            image,instance = helper_pdftojpg(file_instance)

            response = HttpResponse(image.read(),content_type='image/tiff')
            return response
               
    context = {'form':form,'source':source,'converted':converted}
    return render(request, 'convertapp/index.html',context)


def docxtojpg(request):
    """
    This has two steps
    Step 1 -> Converts Word -> PDF
    Step 2 -> Converts PDF -> JPG/tiff
    """
    source = 'Word'
    converted = 'Image'
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save()
            if file_instance.extension != '.docx':
                return render(request,'convertapp/errorfiletype.html')
            
            # Step 1
            pdf,instance = helper_wordtopdf(file_instance)
            # Step  2
            image = helper_pdftojpg(instance)
            response = HttpResponse(image.read(),content_type='image/tiff')
            return response

    context = {'form':form,'source':source,'converted':converted}
    return render(request, 'convertapp/index.html',context)


def imgtopdf(request):
    source = 'Image'
    converted = 'PDF'
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save()
            if file_instance.extension != '.jpg' or file_instance.extension != '.png':
                return render(request,'convertapp/errorfiletype.html')

            pdf,pdf_path = helper_imgtopdf(file_instance)
            response = HttpResponse(pdf,content_type='application/pdf')
            return response

    context = {'form':form,'source':source,'converted':converted}
    return render(request,'convertapp/index.html',context)


def imgtoword(request):
    source = 'Image'
    converted = 'Word'
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save()
            if file_instance.extension != '.jpg' or file_instance.extension != '.png':
                return render(request,'convertapp/errorfiletype.html')

            pdf,pdf_path = helper_imgtopdf(file_instance)
            document,path = helper_pdftoword(pdf_path)

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename = "download.docx"'
            document.save(response)
            return response
    
    
    context = {'form':form,'source':source,'converted':converted}
    return render(request,'convertapp/index.html',context)
