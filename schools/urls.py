"""
holds all school related url paths
"""

from django.urls import path

from schools import views

urlpatterns = [
    # SCHOOL ROUTES
    path('schools/', views.list_schools, name="list-schools"),
    path('schools/<str:school_pk>/get/',
         views.get_school_by_id, name="get-school-by-id"),
    path('schools/add/', views.add_school, name="add-school"),
    path('schools/<str:school_pk>/update/',
         views.update_school, name="update-school"),
    path('schools/<str:school_pk>/delete/',
         views.delete_school, name="delete-school"),

    # SCHOOL DAY ROUTES
    path('school-days/',
         views.SchoolDayList.as_view(), name='school-day-list'),
    path('school-days/<str:school_day_pk>/',
         views.SchoolDayDetail.as_view(), name='school-day-detail'),

    # SCHOOL-USER ROUTES
    path('user-schools/', views.list_user_schools,
         name='get-schools-by-user-access'),
]
