from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News
# Create your views here.

class NewsList(ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = "manyNews"
    


def login(request):
    return render(request, 'news/login.html')

def register(request):
    return render(request, 'news/register.html')

class NewsDetail(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"