from django.urls import path
from . import views

urlpatterns = [
    # GREETING ROUTE
    path('', views.helloWorld, name="hello-world"),
    # USER ROUTES
    path('get-users/', views.getUsers, name="get-users"),
    path('add-user/', views.addUser, name="add-user"),

    # SCHOOL ROUTES
    path('get-schools/<str:pk>/', views.getSchools, name="get-schools-by-owner"),
    path('add-school/', views.addSchool, name="add-school"),
    path('delete-school/<str:pk>/', views.deleteSchool, name="delete-school"),
    path('update-school/<str:pk>/', views.updateSchool, name="update-school"),
    # STUDENT ROUTES
    path('get-students/', views.getStudents, name="get-students"),
    path('get-student/<str:pk>/', views.getStudentById, name="get-student"),
    path('add-student/', views.addStudent, name="add-student"),
    path('update-student/<str:pk>/', views.updateStudent, name="update-student"),
    path('delete-student/<str:pk>/', views.deleteStudent, name="delete-student"),
]
