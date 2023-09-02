from django.urls import include, path

from students.views import student_views




urlpatterns = [

	 # STUDENT ROUTES
	 path('students/', student_views.StudentList.as_view(), name='student-list'),
    # path('students/', student_views.listStudents, name="get-students"),
    # path('students/<str:student_pk>/get/',
    #      student_views.getStudent, name="get-student"),
    # path('students/add/', student_views.addStudent, name="add-student"),
    # path('students/<str:student_pk>/update/',
    #      student_views.updateStudent, name="update-student"),
    # path('students/<str:student_pk>/delete/',
    #      student_views.deleteStudent, name="delete-student"),
]