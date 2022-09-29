from django import forms
from django.forms import ModelForm,FileInput
from .models import File

class FileForm(ModelForm):
    class Meta:
        model = File 
        fields = ('file',)
    
    def __init__(self, *args, **kwargs):
        super(FileForm,self).__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({'class':'form-control','placeholder':'Name'})