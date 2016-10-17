from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models

# Create your views here.

def home(request):
    ui_ctrl = {'index':'active'}

    # news listing
    news_list = models.News.objects.all().order_by("-updated_time")
    paginator = Paginator(news_list, 5) # Show 5 news per page

    page = request.GET.get('page')
    try:
        news_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_page = paginator.page(paginator.num_pages)


    return render(request, 'home.html', locals())

def ReadNews(request,news_id):
    news = models.News.objects.filter(id = news_id).first()
    if not news:
        raise Http404("Not found")
    return render(request,'read_news.html',locals())
