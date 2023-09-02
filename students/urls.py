from django.urls import include, path

from students.views import student_views




urlpatterns = [

	 # STUDENT ROUTES
	 path('students/', student_views.StudentList.as_view(), name='student-list'),
	 path('schools/<str:school_pk>/students/', student_views.StudentList.as_view(), name='student-list'),
	 path('students/<str:student_pk>/', student_views.StudentDetail.as_view(), name='student-detail'),
]