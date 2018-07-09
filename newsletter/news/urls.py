from django.urls import path
from . import views

urlpatterns = [
    path('index', views.NewsList.as_view(), name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]