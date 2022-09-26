from django.db import models
import os

class File(models.Model):
    file = models.FileField(upload_to='uploads')
    name = models.CharField(max_length=200,blank=True)
    extension = models.CharField(max_length=150,blank=True)

    def filename(self):
        return os.path.basename(self.file.name)
    
    def get_extension(self,*args, **kwargs):
        split_tup = os.path.splitext(self.filename())
        file_extension = split_tup[1]
        return file_extension

    def save(self,*args, **kwargs):
        if not self.name:
            self.name = self.filename()
        
        if not self.extension:
            self.extension = self.get_extension()

        super(File,self).save(*args,**kwargs)


    def __str__(self) -> str:
        return self.name
