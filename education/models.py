from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class edu_model(models.Model):
    category=models.CharField(max_length=200,default="none")
    topic=models.CharField(max_length=200)
    text=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    


