from django.urls import path

from students.views import student_views, views


urlpatterns = [
    # STUDENT ROUTES
    # path('students/', student_views.StudentList.as_view(), name='student-list'),
    path('students/', views.list_students, name="student-list"),



    path('students/<str:student_pk>/', views.get_student_by_id, name="student-detail"),
    # path('students/<str:student_pk>/', views.add_student_by_id, name="get-student-by-id")
    # path('students/<str:student_pk>/',
    #      student_views.StudentDetail.as_view(), name='student-detail'),
]
