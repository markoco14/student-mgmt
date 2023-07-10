from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    # GREETING ROUTE
    path('', views.helloWorld, name="hello-world"),

    # AUTH ROUTES
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # USER ROUTES
    path('get-users/', views.getUsers, name="get-users"),
    path('add-user/', views.addUser, name="add-user"),

    # SCHOOL ROUTES
    path('get-schools/<str:pk>/', views.getSchools, name="get-schools-by-owner"),
    path('add-school/', views.addSchool, name="add-school"),
    path('delete-school/<str:pk>/', views.deleteSchool, name="delete-school"),
    path('update-school/<str:pk>/', views.updateSchool, name="update-school"),

    # CLASS ROUTES
    path('get-classes/', views.getClasses, name="get-classes"),
    path('get-class-by-id/<str:pk>', views.getClassById, name="get-class-by-id"),
    path('add-class/', views.addClass, name="add-class"),
    path('register-student-in-class/', views.registerStudentInClass, name='register-student'),
    path('get-students-by-class/<str:pk>/', views.listStudentsByClass, name="list-students-by-class"),
    path('remove-student-from-class/<str:class_pk>/<str:student_pk>/', views.removeStudentFromClassStudentById, name="remove-student"),

    # STUDENT ROUTES
    path('get-students/', views.getStudents, name="get-students"),
    path('get-student/<str:pk>/', views.getStudentById, name="get-student"),
    path('get-students-by-school/<str:pk>/', views.getStudentsBySchoolId, name="get-students-by-school"),
    path('get-students-by-owner/<str:pk>/', views.getStudentsByOwner, name="get-students-by-owner"),
    path('add-student/', views.addStudent, name="add-student"),
    path('update-student/<str:pk>/', views.updateStudent, name="update-student"),
    path('delete-student/<str:pk>/', views.deleteStudent, name="delete-student"),


    # REPORT ROUTES
    path('get-reports-all/', views.getReportsAll, name="get-reports-all"),
    path('get-today-report-by-student-id/<str:pk>', views.getTodayReportByStudentId, name="get-today-report-by-student-id"),
    path('create-report/', views.createReport, name="create-report"),
    path('update-report/<str:pk>/', views.updateReport, name="update-report"),
    path('delete-report/<str:pk>/', views.deleteReport, name="delete-report"),
]
