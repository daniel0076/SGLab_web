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

def teacher(request):

    teacher = models.Teacher.objects.all().first()
    edu = models.TeacherEducation.objects.all().order_by('-order')
    exp = models.TeacherExp.objects.all().order_by('-order')
    awards = models.TeacherAwards.objects.all().order_by('-order')
    mem = models.TeacherMember.objects.all().order_by('-order')
    ui_ctrl={'teacher':'active'}

    return render(request, 'teacher.html', locals())

def publications(request):
    teacher = models.Teacher.objects.all().first()
    journal_paper = models.TeacherPublication.objects.filter(category='journal_paper').order_by('-date')
    conf_paper = models.TeacherPublication.objects.filter(category='conf_paper').order_by('-date')
    book_chapter = models.TeacherPublication.objects.filter(category='book_chapter').order_by('-date')

    ui_ctrl={'publications':'active'}
    return render(request, 'publications.html', locals())

