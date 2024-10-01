from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>prova_p1</h1>')


# Create your views here.
