from django.contrib import admin
from django.urls import path
from . import views

# Espace de nom
app_name = 'blog'

urlpatterns = [
    path('', views.BlogHome.as_view(), name='home'),
    path('create/', views.BlogPostCreate.as_view(), name='create'),
    path('update/<str:slug>/', views.BlogPostUpdate.as_view(), name='update'),
    path('<str:slug>/', views.BlogPostDetail.as_view(), name='post'),
    path('delete/<str:slug>/', views.BlogPostDelete.as_view(), name='delete'),
    path('article-<str:num_art>/', views.article, name='article'),
]