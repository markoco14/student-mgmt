from django.urls import path
from . import views

urlpatterns = [
    # GREETING ROUTE
    path('', views.helloWorld, name="hello-world"),
    # SCHOOL ROUTES
    path('list-schools/', views.listSchools, name="list-schools"),
    # STUDENT ROUTES
    path('get-students/', views.getStudents, name="get-students"),
    path('get-student/<str:pk>/', views.getStudentById, name="get-student"),
    path('add-student/', views.addStudent, name="add-student"),
    path('update-student/<str:pk>/', views.updateStudent, name="update-student"),
    path('delete-student/<str:pk>/', views.deleteStudent, name="delete-student"),
]
