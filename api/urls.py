from django.urls import include, path

from .views import views
from .views import user_views
from .views import jwt_views
from .views import school_views
from .views import report_views
from .views import schedule_views
from curriculum.views import curriculum_views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'subjects', curriculum_views.SubjectViewSet,
                basename='subject')

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


    # SCHOOL ROUTES
    path('schools/', school_views.listSchools, name="list-schools"),
    path('schools/<str:school_pk>/get/',
         school_views.getSchoolById, name="get-school-by-id"),
    path('schools/add/', school_views.addSchool, name="add-school"),
    path('schools/<str:school_pk>/update/',
         school_views.updateSchool, name="update-school"),
    path('schools/<str:school_pk>/delete/',
         school_views.deleteSchool, name="delete-school"),

    # SCHOOL DAY ROUTES
    path('schools/<str:school_pk>/days/',
         school_views.SchoolDayList.as_view(), name='school-day-list'),
    path('schools/days/<str:school_day_pk>/',
         school_views.SchoolDayDetail.as_view(), name='school-day-detail'),

    # SCHOOL-USER ROUTES
    path('users/<str:user_pk>/schools/', school_views.listUserSchools,
         name='get-schools-by-user-access'),


    # SCHOOL-TEACHER ROUTES
    path('schools/<str:school_pk>/teachers/',
         user_views.listSchoolTeachers, name="list-school-teachers"),

	# SCHOOL-ADMIN ROUTES
	path('schools/<str:school_pk>/admins/', user_views.listSchoolAdmins, name='list-school-admins'),
    path('/users/admins/add/', user_views.addAdmin, name="add-admin"),


   

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



    # ViewSetRoutes
    path('', include(router.urls)),

    # SCHEDULE ROUTES
    path('weekdays/', schedule_views.getWeekdays, name='weekday'),

]