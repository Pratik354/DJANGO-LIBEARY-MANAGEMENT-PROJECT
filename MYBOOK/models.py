

from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bookapp(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 id=models.AutoField(primary_key=True)

 stud_id=models.CharField(max_length=100)
 book_name=models.CharField(max_length=100)
 auther_name=models.CharField(max_length=100,null=True,blank=True)
 status=models.CharField(max_length=100,default="pending")
 date=models.DateTimeField(auto_now_add=True)

 def __str__(self):
        return self.stud_id




