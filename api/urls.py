"""
contain general urls
"""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from .views import views
from .views import user_views
from .views import jwt_views
from .views import report_views
from .views import schedule_views


urlpatterns = [
    # GREETING ROUTE
    path('', views.helloWorld, name="hello-world"),


    # AUTH ROUTES
    path('token/', jwt_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # USER ROUTES
    path('users/', user_views.getUsers, name="get-users"),
    path('users/<str:user_pk>/get/',
         user_views.getUserProfileById, name="get-user-profile"),
    path('users/add/', user_views.addUser, name="add-user"),
    path('users/<str:user_pk>/update/',
         user_views.updateUser, name="update-user"),
    path('users/<str:user_pk>/change-password/',
         user_views.changePassword, name="change-password"),


    # TEACHER-USER ROUTES
    path('teachers/', user_views.listTeachers, name="get-users"),
    path('users/teachers/add/', user_views.addTeacher, name="add-teacher"),




    #
    # REPORT ROUTES
    #
    path('reports/', report_views.listReports, name="list-reports"),
    path('classes/<str:class_pk>/reports/date/<str:date_pk>/',
         report_views.getReportByClassAndDate, name="get-report-by-date"),
    path('reports/create/', report_views.createReportAndReportDetails,
         name="create-report"),
    path('reports/<str:pk>/delete/',
         report_views.deleteReport, name="delete-report"),


    # REPORT DETAILS ROUTES
    path('reports/<str:report_pk>/details/',
         report_views.listReportsDetailsByReportId, name="get-report-details"),
    # path('reports/details/create/', report_views.createReportDetails, name="create-report-details"),
    path('reports/details/<str:detail_pk>/',
         report_views.updateReportDetails, name="delete-report-details"),
    # path('reports/details/<str:detail_pk>/delete/', report_views.deleteReportDetails, name="delete-report-details"),

    # SCHEDULE ROUTES
    path('weekdays/', schedule_views.getWeekdays, name='weekday'),

]
