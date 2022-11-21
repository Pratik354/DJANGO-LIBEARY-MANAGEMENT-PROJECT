from django.db import models




from distutils.command.upload import upload


# Create your models here.
class courser(models.Model):
 image=models.ImageField(upload_to='IMAGE')
 date=models.DateTimeField(auto_now_add=True)
 def __str__(self):
        return str(self.image)

class image(models.Model):
 IMAGE=models.ImageField(upload_to='IMAGE')
 date=models.DateTimeField(auto_now_add=True)
 def __str__(self):
        return str(self.IMAGE)
    


    
