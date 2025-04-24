from django.shortcuts import render
from django.http import HttpResponse    


def home(request):
    return render(request, 'home.html')

def contato(request):
    return HttpResponse('CONTATO PAGE')

def sobre(request):
    return HttpResponse('SOBRE PAGE')


