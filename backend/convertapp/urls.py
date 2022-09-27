from django.urls import path
from .views import pdftodocx,docxtopdf,pdftojpg,docxtojpg,imgtopdf 

urlpatterns = [
    path("",imgtopdf,name='index')
]
