from django.urls import path
from .views import pdftodocx,docxtopdf

urlpatterns = [
    path("",docxtopdf,name='index')
]
