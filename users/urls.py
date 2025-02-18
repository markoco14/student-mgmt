"""
contain general urls
"""

from django.urls import path

from users import views

urlpatterns = [
    path('users/', views.getUsers, name="get-users"),
    path('users/<str:user_pk>/get/', views.getUserProfileById, name="get-user-profile"),
    path('users/add/', views.addUser, name="add-user"),
    path('users/<str:user_pk>/update/', views.updateUser, name="update-user"),
    path('users/<str:user_pk>/change-password/', views.changePassword, name="change-password"),
]