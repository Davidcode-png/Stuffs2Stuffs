from django.urls import path
from .views import imgtopdf,index

urlpatterns = [
    path("",index,name='index')
]
