
from django.shortcuts import render

def home(request):
    return render(request, 'shoe_brands/home.html')

def info(request):
    return render(request, 'shoe_brands/info.html')

def contact(request):
    return render(request, 'shoe_brands/contact.html')
