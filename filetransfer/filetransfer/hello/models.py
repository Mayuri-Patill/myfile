from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class file(models.Model):
    uploadingdate=models.CharField(max_length=30,null=True)
    uploadfile=models.FileField(null=True)
    filetype=models.CharField(max_length=30,null=True)
    description=models.CharField(max_length=200,null=True)


def __str__(self):
    return self.user