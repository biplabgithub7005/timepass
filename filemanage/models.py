from django.db import models

# Create your models here.
class FileUpload(models.Model):
    file_name = models.CharField(max_length=100,default='file title')
    file_path =models.FileField(default="sample.pdf", upload_to="files")
    file_date =models.DateField(auto_now_add=True)
    file_desc = models.CharField(max_length=100, default='This is your file for download click download button')

    def __str__(self):
        return self.file_name+""+str(self.pk)