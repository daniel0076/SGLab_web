from django.shortcuts import render
from . import models

# Create your views here.

def research(request):
    articles = models.Research.objects.all().order_by('order')
    ui_ctrl = {'research':'active'}
    return render(request, 'index.html', locals())

def home(request):
    ui_ctrl = {'home':'active'}
    return render(request, 'home.html', locals())
