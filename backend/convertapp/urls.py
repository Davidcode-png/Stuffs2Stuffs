from django.urls import path
from .views import index,pdftodocx,docxtopdf,pdftojpg,docxtojpg,imgtopdf,imgtoword

urlpatterns = [
    path("",index,name='index')
]
