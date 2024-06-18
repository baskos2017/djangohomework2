from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')

def book(request, title):
    context = {'title': title}
    return render(request, 'book.html', context)


