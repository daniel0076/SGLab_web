from django.shortcuts import render

# Create your views here.

def home(request):
    ui_ctrl = {'index':'active'}
    return render(request, 'home.html', locals())
