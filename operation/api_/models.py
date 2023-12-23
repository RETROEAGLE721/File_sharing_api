from django.db import models
from datetime import datetime

class Users(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False, blank=False)
    password = models.CharField(max_length=15, blank=False,default="Apo")
    
    def __str__(self) -> str:
        return self.name

class operation(models.Model):
    name = models.CharField(max_length=15, unique=True, null=False, blank=False)
    password = models.CharField(max_length=15, blank=False,default="Apo")
    
    def __str__(self) -> str:
        return self.name

class file_datas(models.Model):
    id = models.CharField(max_length=100,unique=True, null=False,primary_key=True, blank=False)
    name = models.FileField()
    file_url = models.URLField(max_length=200, default="")
    date = models.DateTimeField(null=False, blank=False,default=datetime.now())
    
    def __str__(self) -> str:
        return self.name