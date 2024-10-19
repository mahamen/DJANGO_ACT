
from django.shortcuts import render

def home(request):
    return render(request, 'animals/home.html')

def info(request):
    return render(request, 'animals/info.html')

def contact(request):
    return render(request, 'animals/contact.html')
