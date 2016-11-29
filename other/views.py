from django.shortcuts import render
from .models import ExternalLinks

# Create your views here.

def external_links(request):
    links = ExternalLinks.objects.all()
    return render(request, 'links.html', locals())

