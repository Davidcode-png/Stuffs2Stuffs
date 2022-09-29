from pydoc import doc
from django.urls import path
from .views import index,pdftodocx,docxtopdf,pdftojpg,docxtojpg,imgtopdf,imgtoword

urlpatterns = [
    path("",index,name='index'),
    path("pdftodocx/",pdftodocx,name='ptd'),
    path("docxtopdf/",docxtopdf,name='dtp'),
    path("pdftoimg/",pdftojpg,name='pti'),
    path("docxtoimg/",docxtojpg,name='dti'),
    path("imgtopdf",imgtopdf,name='itp'),
    path("imgtoword",imgtoword,name='itd'),

]
