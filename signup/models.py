from django.db import models
class mygroove(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    mobileno=models.CharField(max_length=50)   

