from django.urls import include, path

from classes.views import classes_views, class_students_views

urlpatterns = [
    # CLASS ROUTES
    path('schools/<str:school_pk>/classes/',
         classes_views.ClassEntityList.as_view(), name="class-list"),
    path('classes/', classes_views.ClassEntityList.as_view(), name="class-list"),
    path('classes/<str:class_entity_pk>/', classes_views.ClassEntityDetail.as_view(), name='class-detail'),
	
    # CLASS STUDENT ROUTES
    path('class-students/', class_students_views.ClassStudentList.as_view(), name="class-student-list"),
    path('class-students/<str:class_student_pk>/', class_students_views.ClassStudentDetail.as_view(), name="class-student-detail"),
]