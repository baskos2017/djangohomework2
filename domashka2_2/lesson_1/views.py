from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def index(request):
    return render(request, 'lesson_1/index.html')

def subpage(request, subpage):
    context = {'subpage': subpage}
    return render(request, 'lesson_1/subpage.html', context)
