import os
from django.shortcuts import render,HttpResponse
from .forms import FileForm
from .utils import helper_imgtopdf, helper_pdftoword,helper_pdftojpg ,helper_wordtopdf


def pdftodocx(request):
    form  = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.save()
            document,path = helper_pdftoword(file)
            
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
            pdf = helper_wordtopdf(file_instance)
            
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=download.pdf'
            return response
            

    
    context = {'form':form}
    
    return render(request, 'convertapp/index.html',context)



def pdftojpg(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save()
            image,instance = helper_pdftojpg(file_instance)

            response = HttpResponse(image.read(),content_type='image/tiff')
            return response
               
    context = {'form':form}
    return render(request, 'convertapp/index.html',context)


def docxtojpg(request):
    """
    This has two steps
    Step 1 -> Converts Word -> PDF
    Step 2 -> Converts PDF -> JPG/tiff
    """
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save()
            
            # Step 1
            pdf,instance = helper_wordtopdf(file_instance)
            # Step  2
            image = helper_pdftojpg(instance)
            response = HttpResponse(image.read(),content_type='image/tiff')
            return response

    context = {'form':form}
    return render(request, 'convertapp/index.html',context)


def imgtopdf(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            file_instance = form.save()
            pdf = helper_imgtopdf(file_instance)
            response = HttpResponse(pdf,content_type='application/pdf')
            return response

    context = {'form':form}
    return render(request,'convertapp/index.html',context)