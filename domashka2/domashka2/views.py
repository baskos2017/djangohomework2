#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request):
    return render(request, 'home.html')

def book(request, title):
    context = {'title': title}
    return render(request, 'book.html', context)


