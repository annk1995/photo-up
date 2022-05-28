from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request,'gallery.html')

def viewPhoto(request,pk):
    return render(request,'photo.html')

def addPhoto(request):
    return render(request,'add.html')