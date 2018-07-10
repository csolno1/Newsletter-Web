from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News, Tag
# Create your views here.

class NewsList(ListView):
    model = News
    template_name = "news/index.html"
    context_object_name = "manyNews"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['all_tag'] = True
        context['favorite_tag'] = False
        context['cur_tag'] = None
        return context
    
class NewsTagDetail(DetailView):
    model = Tag
    template_name = "news/index.html"
    context_object_name = "cur_tag"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['all_tag'] = False
        context['favorite_tag'] = False
        context['manyNews'] = super().get_object().news.all()
        return context

def login(request):
    return render(request, 'news/login.html')

def register(request):
    return render(request, 'news/register.html')

class NewsDetail(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"