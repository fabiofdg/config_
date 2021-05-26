#é onde lidamos com a lógica de solicitação / resposta para nosso aplicativo da web
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def homePageView(request):
    return HttpResponse('<h1>Hello, World!!</h1>')

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BasePageView(TemplateView):
    template_name = 'base.html'