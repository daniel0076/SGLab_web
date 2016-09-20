from django.shortcuts import render
from . import models

# Create your views here.


def members(request):
    postdoc = models.Member.objects.filter(identity='Postdoc')\
                .order_by('name_en')
    master = models.Member.objects.filter(identity='Master Student')
    phd = models.Member.objects.filter(identity='PhD Student')
    assistant = models.Member.objects.filter(identity='Assistant')

    members = {
        'postdoc': postdoc,
        'phd' : phd,
        'master' : master,
        'assistant': assistant,
    }

    ui_ctrl={'members':'active'}

    return render(request, 'members.html', locals())
