"""
holds all school related url paths
"""

from django.urls import path
from api.views import user_views

from schools import school_views



urlpatterns = [
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
    path('users/admins/add/', user_views.addAdmin, name="add-admin"),
]
