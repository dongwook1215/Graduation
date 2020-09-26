from django.shortcuts import render, get_object_or_404, redirect
from .models import Cloud
from datetime import date
from .models import User
# Create your views here.

def upload_cloud(request):
    if request.method =="POST":
        subject = request.POST['subject']
        file = request.FILES['file']
        filetype = request.POST['filetype']
        description = request.POST['description']
        ct = User.objects.filter(username=request.user.username).first()
        try:
            Cloud.objects.create(uploadingdate=date.today(),subject=subject,file=file,filetype=filetype,description=description,user=ct)
        except:
            pass 
    cloud = Cloud.objects.all().filter(user=request.user.id)
    return render(request, 'upload_cloud.html',{'cloud':cloud})    

def delete_file(request):
    if request.method == 'POST':
        cloud = Cloud.objects.get()
        cloud.delete()
    return render(request, 'upload_cloud.html',{'cloud':cloud}) 
