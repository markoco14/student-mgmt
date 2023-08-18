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

    # SCHOOL-USER ROUTES
    path('users/<str:user_pk>/schools/', school_views.listUserSchools, name='get-schools-by-user-access'),
    
    # SCHOOL-TEACHER ROUTES
    path('schools/<str:school_pk>/teachers/', school_views.getSchoolTeachers, name="get-teachers-by-school"),

    # SCHOOL-CLASS ROUTES
    path('schools/<str:school_pk>/classes/', class_views.listSchoolClasses, name="list-school-classes"),
    path('schools/<str:school_pk>/classes/day/<str:day_pk>/', class_views.listSchoolTodayClasses, name='list-school-today-classes'),

    # SCHOOL-STUDENT ROUTES
    path('schools/<str:school_pk>/students/', student_views.listSchoolStudents, name="get-students-by-school"),

    # CLASS ROUTES
    path('classes/', class_views.listClasses, name="list-classes"),
    path('classes/<str:class_pk>/get/', class_views.getClassById, name="get-class"),
    path('classes/add/', class_views.addClass, name="add-class"),
    path('classes/<str:class_pk>/delete/', class_views.deleteClass, name="delete-class"),

    # CLASS-STUDENT ROUTES
    path('classes/<str:class_pk>/students/', student_views.listClassStudents, name="list-class-students"),
    path('classes/students/add/', class_views.addClassStudent, name='add-class-student'),
    path('classes/<str:class_pk>/students/<str:student_pk>/delete/', class_views.deleteClassStudent, name="delete-class-student"),


    # STUDENT ROUTES
    path('students/', student_views.listStudents, name="get-students"),
    path('students/<str:student_pk>/get/', student_views.getStudent, name="get-student"),
    path('students/add/', student_views.addStudent, name="add-student"),
    path('students/<str:student_pk>/update/', student_views.updateStudent, name="update-student"),
    path('students/<str:student_pk>/delete/', student_views.deleteStudent, name="delete-student"),

    # 
    # REPORT ROUTES
    # 
    path('reports/', report_views.listReports, name="list-reports"),
    path('classes/<str:class_pk>/reports/date/<str:date_pk>/', report_views.getReportByClassAndDate, name="get-report-by-date"),
    path('reports/create/', report_views.createReportAndReportDetails, name="create-report"),
    path('reports/<str:pk>/delete/', report_views.deleteReport, name="delete-report"),
    
    # TODO: STUDENT-REPORT ROUTES FOR LATER 
    # path('students/<str:student_pk>/reports/', report_views.getTodayReportByStudentId, name="get-today-report-by-student-id"),
    # path('get-today-report-by-student-id/<str:pk>/', report_views.getTodayReportByStudentId, name="get-today-report-by-student-id"),


    # REPORT DETAILS ROUTES
    path('get-report-details-by-report-id/<str:report_pk>/', report_views.getReportsDetailsByReportId, name="get-report-details"),
    path('create-report-details/', report_views.createReportDetails, name="create-report-details"),
    path('delete-report-details/<str:pk>/', report_views.deleteReportDetails, name="delete-report-details"),
    path('update-report-details/<str:pk>/', report_views.updateReportDetails, name="delete-report-details"),


    # ADMIN ROUTES
    path('schools/<str:school_pk>/levels/', admin_views.listSchoolLevels, name='list-school-levels'),
    path('levels/add', admin_views.addLevel, name='add-level'),
    path('levels/<str:level_pk>/delete/', admin_views.deleteLevel, name='delete-level'),

]
