from django.shortcuts import render
from .models import Category,Photo

# Create your views here.
def gallery(request):
    categories =Category.objects.all()
    return render(request,'gallery.html')

def viewPhoto(request,pk):
    return render(request,'photo.html')

def addPhoto(request):
    return render(request,'add.html')