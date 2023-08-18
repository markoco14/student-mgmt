from django.urls import path

from .views import views, user_views, jwt_views, school_views, class_views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    # GREETING ROUTE
    path('', views.helloWorld, name="hello-world"),

    # AUTH ROUTES
    path('token/', jwt_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # USER ROUTES
    path('get-users/', user_views.getUsers, name="get-users"),
    path('users/<str:user_pk>/get/', user_views.getUserProfileById, name="get-user-profile"),
    path('add-user/', user_views.addUser, name="add-user"),
    path('users/<str:user_pk>/update/', user_views.updateUser, name="update-user"),
    path('users/<str:user_pk>/change-password/', user_views.changePassword, name="change-password"),
    path('add-teacher/', user_views.addTeacher, name="add-teacher"),
    path('get-teachers-by-school/<str:school_pk>/<str:owner_pk>/', user_views.getTeachersBySchool, name="get-teachers-by-school"),

    # SCHOOL ROUTES
    path('get-schools/<str:pk>/', school_views.getSchools, name="get-schools-by-owner"),
    path('add-school/', school_views.addSchool, name="add-school"),
    path('delete-school/<str:pk>/', school_views.deleteSchool, name="delete-school"),
    path('update-school/<str:pk>/', school_views.updateSchool, name="update-school"),

    # SCHOOL USER ROUTES
    path('get-schools-by-user-access/<str:pk>/', views.getSchoolsByUserAccess, name='get-schools-by-user-access'),

    # CLASS ROUTES
    path('get-classes/', class_views.getClasses, name="get-classes"),
    path('get-classes-by-school-id/<str:pk>/', class_views.getClassesBySchoolId, name="get-classes-by-school-id"),
    path('get-class-by-id/<str:pk>/', class_views.getClassById, name="get-class-by-id"),
    path('get-classes-by-school-and-date/<str:school_pk>/<str:date_pk>/', class_views.getClassBySchoolAndDate, name='get-classes-by-school-and-date'),
    path('get-classes-with-class-lists/', class_views.getClassesWithClassLists, name="classes-with-class-lists"),
    path('add-class/', class_views.addClass, name="add-class"),
    path('delete-class/<str:pk>/', class_views.deleteClass, name="delete-class"),


    # CLASS STUDENT REGISTRATION ROUTES
    path('register-student-in-class/', views.registerStudentInClass, name='register-student'),
    path('remove-student-from-class/<str:class_pk>/<str:student_pk>/', views.removeStudentFromClassStudentById, name="remove-student"),


    # STUDENT ROUTES
    path('get-students-by-class/<str:pk>/', views.listStudentsByClass, name="list-students-by-class"),
    path('get-students/', views.getStudents, name="get-students"),
    path('get-student/<str:pk>/', views.getStudentById, name="get-student"),
    path('get-students-by-school/<str:pk>/', views.getStudentsBySchoolId, name="get-students-by-school"),
    path('get-students-by-owner/<str:pk>/', views.getStudentsByOwner, name="get-students-by-owner"),
    path('add-student/', views.addStudent, name="add-student"),
    path('update-student/<str:pk>/', views.updateStudent, name="update-student"),
    path('delete-student/<str:pk>/', views.deleteStudent, name="delete-student"),


    # REPORT ROUTES
    path('get-reports-all/', views.getReportsAll, name="get-reports-all"),
    path('get-report-by-date/<str:class_pk>/<str:date_pk>/', views.getReportByClassAndDate, name="get-report-by-date"),
    path('get-today-report-by-student-id/<str:pk>/', views.getTodayReportByStudentId, name="get-today-report-by-student-id"),
    path('create-report/', views.createReportAndReportDetails, name="create-report"),
    path('delete-report/<str:pk>/', views.deleteReport, name="delete-report"),


    # REPORT DETAILS ROUTES
    path('get-report-details-by-report-id/<str:report_pk>/', views.getReportsDetailsByReportId, name="get-report-details"),
    path('create-report-details/', views.createReportDetails, name="create-report-details"),
    path('delete-report-details/<str:pk>/', views.deleteReportDetails, name="delete-report-details"),
    path('update-report-details/<str:pk>/', views.updateReportDetails, name="delete-report-details"),


    # ADMIN ROUTES
    path('get-levels/', views.getAllLevels, name='get-levels'),
    path('get-levels-by-school-id/<str:pk>/', views.getLevelsBySchoolId, name='get-levels-by-school'),
    path('add-level/', views.addLevel, name='add-level'),
    path('delete-level/<str:pk>/', views.deleteLevel, name='delete-level'),

]
