from django.shortcuts import render
from . import models

# Create your views here.

def research(request):
    ui_ctrl = {'research':'active'}
    return render(request, 'index.html', locals())

def home(request):
    ui_ctrl = {'home':'active'}
    return render(request, 'home.html', locals())

def generic(request):
    return render(request, 'generic.html', locals())
