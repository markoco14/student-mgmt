from django.urls import path

from .views import views, user_views, jwt_views, school_views, class_views, student_views, report_views, admin_views
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
    path('users/', user_views.getUsers, name="get-users"),
    path('users/<str:user_pk>/get/', user_views.getUserProfileById, name="get-user-profile"),
    path('users/add/', user_views.addUser, name="add-user"),
    path('users/<str:user_pk>/update/', user_views.updateUser, name="update-user"),
    path('users/<str:user_pk>/change-password/', user_views.changePassword, name="change-password"),

    # TEACHER-USER ROUTES
    path('users/teachers/add/', user_views.addTeacher, name="add-teacher"),

    # SCHOOL ROUTES
    path('schools/', school_views.listSchools, name="list-schools"),
    path('schools/<str:school_pk>/get/', school_views.getSchoolById, name="get-school-by-id"),
    path('schools/add/', school_views.addSchool, name="add-school"),
    path('schools/<str:school_pk>/update/', school_views.updateSchool, name="update-school"),
    path('schools/<str:school_pk>/delete/', school_views.deleteSchool, name="delete-school"),

    # SCHOOL USER ROUTES
    path('users/<str:user_pk>/schools/', school_views.listUserSchools, name='get-schools-by-user-access'),
    
    # SCHOOL TEACHER ROUTES
    path('schools/<str:school_pk>/teachers/', school_views.getSchoolTeachers, name="get-teachers-by-school"),


    # CLASS ROUTES
    path('get-classes/', class_views.getClasses, name="get-classes"),
    path('get-classes-by-school-id/<str:pk>/', class_views.getClassesBySchoolId, name="get-classes-by-school-id"),
    path('get-class-by-id/<str:pk>/', class_views.getClassById, name="get-class-by-id"),
    path('get-classes-by-school-and-date/<str:school_pk>/<str:date_pk>/', class_views.getClassBySchoolAndDate, name='get-classes-by-school-and-date'),
    path('get-classes-with-class-lists/', class_views.getClassesWithClassLists, name="classes-with-class-lists"),
    path('add-class/', class_views.addClass, name="add-class"),
    path('delete-class/<str:pk>/', class_views.deleteClass, name="delete-class"),


    # CLASS STUDENT REGISTRATION ROUTES
    path('register-student-in-class/', class_views.registerStudentInClass, name='register-student'),
    path('remove-student-from-class/<str:class_pk>/<str:student_pk>/', class_views.removeStudentFromClassStudentById, name="remove-student"),


    # STUDENT ROUTES
    path('get-students/', student_views.getStudents, name="get-students"),
    path('get-student/<str:pk>/', student_views.getStudentById, name="get-student"),
    path('get-students-by-school/<str:pk>/', student_views.getStudentsBySchoolId, name="get-students-by-school"),
    path('get-students-by-owner/<str:pk>/', student_views.getStudentsByOwner, name="get-students-by-owner"),
    path('get-students-by-class/<str:pk>/', student_views.listStudentsByClass, name="list-students-by-class"),
    path('add-student/', student_views.addStudent, name="add-student"),
    path('update-student/<str:pk>/', student_views.updateStudent, name="update-student"),
    path('delete-student/<str:pk>/', student_views.deleteStudent, name="delete-student"),


    # REPORT ROUTES
    path('get-reports-all/', report_views.getReportsAll, name="get-reports-all"),
    path('get-report-by-date/<str:class_pk>/<str:date_pk>/', report_views.getReportByClassAndDate, name="get-report-by-date"),
    path('get-today-report-by-student-id/<str:pk>/', report_views.getTodayReportByStudentId, name="get-today-report-by-student-id"),
    path('create-report/', report_views.createReportAndReportDetails, name="create-report"),
    path('delete-report/<str:pk>/', report_views.deleteReport, name="delete-report"),


    # REPORT DETAILS ROUTES
    path('get-report-details-by-report-id/<str:report_pk>/', report_views.getReportsDetailsByReportId, name="get-report-details"),
    path('create-report-details/', report_views.createReportDetails, name="create-report-details"),
    path('delete-report-details/<str:pk>/', report_views.deleteReportDetails, name="delete-report-details"),
    path('update-report-details/<str:pk>/', report_views.updateReportDetails, name="delete-report-details"),


    # ADMIN ROUTES
    path('get-levels/', admin_views.getAllLevels, name='get-levels'),
    path('get-levels-by-school-id/<str:pk>/', admin_views.getLevelsBySchoolId, name='get-levels-by-school'),
    path('add-level/', admin_views.addLevel, name='add-level'),
    path('delete-level/<str:pk>/', admin_views.deleteLevel, name='delete-level'),

]
