"""
holds all school related url paths
"""

from django.urls import path
from api.views import user_views

from schools import school_views



urlpatterns = [
    # SCHOOL ROUTES
    path('schools/', school_views.list_schools, name="list-schools"),
    path('schools/<str:school_pk>/get/',
         school_views.get_school_by_id, name="get-school-by-id"),
    path('schools/add/', school_views.add_school, name="add-school"),
    path('schools/<str:school_pk>/update/',
         school_views.update_school, name="update-school"),
    path('schools/<str:school_pk>/delete/',
         school_views.delete_school, name="delete-school"),

    # SCHOOL DAY ROUTES
    path('school-days/',
         school_views.SchoolDayList.as_view(), name='school-day-list'),
    path('school-days/<str:school_day_pk>/',
         school_views.SchoolDayDetail.as_view(), name='school-day-detail'),

    # SCHOOL-USER ROUTES
    path('user-schools/', school_views.list_user_schools,
         name='get-schools-by-user-access'),


    # SCHOOL-TEACHER ROUTES
    path('school-teachers/',
         user_views.listTeachers, name="list-school-teachers"),
	path('users/teachers/add/', user_views.addTeacher, name="add-teacher"),

	# SCHOOL-ADMIN ROUTES
	path('school-admins/', user_views.listAdmins, name='list-school-admins'),
    path('users/admins/add/', user_views.addAdmin, name="add-admin"),
]
