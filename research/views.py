from django.shortcuts import render
from . import models

# Create your views here.

def research(request):
    return render(request, 'research.html', locals())
