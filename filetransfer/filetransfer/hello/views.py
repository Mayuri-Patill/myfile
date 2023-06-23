from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import date
from hello.models import upload
# Create your views here.
def Home (request):
    return render(request,'base.html')
def upload (request):
    if request.method=="POST":
        fileupload = request.FILES['fileupload']
        filetype = request.POST['filetype']
        description = request.POST['description']
        ct = User.objects.filter(User).frist()
        upload=upload(fileupload=fileupload,filetype=filetype,description=description)
        upload.save()
        return render(request,'upload.html')
def download (request):
    files = files.objects.all()
    d = {'files':files}
    return render(request,'download.html')

