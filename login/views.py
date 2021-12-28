from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'index.html')


def aboutus(request):
    return render(request,'about-us.html')


def contact(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'blog.html')

def classes(request):
    return render(request, 'classes.html')