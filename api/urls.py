from django.urls import path
from . import views

urlpatterns = [

    path('get-items', views.getItems),
    path('add-item/', views.addItem),
    path('delete-item/<str:pk>/', views.deleteItem),

    path('get-posts/', views.getPosts),
    path('add-post/', views.addPost),
    path('delete-post/<str:pk>/', views.deletePost, name="post-delete"),

    path('get-students/', views.getStudents, name="get-students"),
    path('get-student/<str:pk>/', views.getStudentById, name="get-student"),
    path('add-student/', views.addStudent, name="add-student"),
    path('update-student/<str:pk>/', views.updateStudent, name="update-student"),
    path('delete-student/<str:pk>/', views.deleteStudent, name="delete-student"),
]