from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def skf(request):
    return HttpResponse('shashank sen')


def index(request):
    return render(request,'index.html')    