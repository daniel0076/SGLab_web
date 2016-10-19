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
    edu = models.TeacherEducation.objects.all()
    exp = models.TeacherExp.objects.all()
    awards = models.TeacherAwards.objects.all()
    mem = models.TeacherMember.objects.all()
    ui_ctrl={'teacher':'active'}

    return render(request, 'teacher.html', locals())

def publications(request):
    teacher = models.Teacher.objects.all().first()
    journal_paper = models.TeacherPublication.objects.filter(category='journal_paper')
    conf_paper = models.TeacherPublication.objects.filter(category='conf_paper')
    book_chapter = models.TeacherPublication.objects.filter(category='book_chapter')
    ui_ctrl={'publications':'active'}
    return render(request, 'publications.html', locals())

