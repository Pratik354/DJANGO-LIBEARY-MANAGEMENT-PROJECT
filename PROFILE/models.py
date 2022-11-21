
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
 user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
 
 
 stud_id=models.CharField(max_length=100,null=True,blank=True)
 email=models.EmailField(max_length=100,null=True,blank=True)
 number=models.IntegerField(null=True,blank=True)
 dob=models.DateField(null=True,blank=True)
 gender=models.CharField(max_length=100,null=True,blank=True)
 branch=models.CharField(max_length=100,null=True,blank=True)
 semister=models.CharField(max_length=100,null=True,blank=True)
 photo=models.ImageField(upload_to='IMAGE',default='path/static/media/A.jpg')
 date=models.DateTimeField(auto_now_add=True,null=True,blank=True)

 def __str__(self):
        return self.stud_id




