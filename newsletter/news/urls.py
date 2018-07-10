from django.urls import path
from . import views

urlpatterns = [
    path('index', views.NewsList.as_view(), name='index'),
    path('index/<int:pk>', views.NewsTagDetail.as_view(), name='tag-detail'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('details/<int:pk>', views.NewsDetail.as_view(), name='news-details')
]