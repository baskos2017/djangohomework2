from django.shortcuts import render
from django.http import HttpRequest


def index(request):
    return render(request, 'index.html')

def bio(request, username):
    context = {'username': username}
    return render(request, 'bio.html', context)