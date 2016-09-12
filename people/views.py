from django.shortcuts import render
from . import models

# Create your views here.


def members(request):
    postdoc = models.Member.objects.filter(identity='Postdoc')\
                .order_by('name_en')
    master = models.Member.objects.filter(identity='Master Student')
    phd = models.Member.objects.filter(identity='PhD Student')
    assistant = models.Member.objects.filter(identity='Assistant')

    member_groups = [
        {'title': 'Postdoc', 'members': postdoc},
        {'title': 'PhD Student', 'members': phd},
        {'title': 'Master Student', 'members': master},
        {'title': 'Assistant', 'members': assistant},
    ]

    return render(request, 'members.html', locals())
