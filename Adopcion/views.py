from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Adopcion

# Create your views here.
def index(request):
    misAdopciones = Adopcion.objects.all()
    template = loader.get_template('index.html')
    context = {
        'misAdopciones' : misAdopciones
    }
    return HttpResponse(template.render(context, request))