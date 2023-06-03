from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('posts/', views.getPosts),
    path('add-post', views.addPost),
]