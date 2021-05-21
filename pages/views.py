#é onde lidamos com a lógica de solicitação / resposta para nosso aplicativo da web
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('<h1>Hello, World!!</h1>')