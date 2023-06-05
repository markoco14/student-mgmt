from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addItem),
    path('posts/', views.getPosts),
    path('add-post/', views.addPost),
    path('get-students/', views.getStudents),
    path('add-student/', views.addStudent),
    path('delete-student/<str:pk>/', views.deleteStudent, name="student-delete"),
]