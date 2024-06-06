# app_blog/urls.py
from django.urls import path
from app_blog import views
from django.urls import reverse
urlpatterns = [
    path(r'', views.HomePageView.as_view(), name='articles-list'),
]
