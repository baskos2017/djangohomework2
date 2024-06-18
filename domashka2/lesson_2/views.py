from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'lesson_2/index.html')

def subpage(request, subpage):
    context = {'subpage': subpage}
    return render(request, 'lesson_2/subpage.html', context)
