from django.urls import include, path

from classes.views import class_assessment_views, classes_views, class_students_views, views

urlpatterns = [
    # CLASS ROUTES
    path("classes/", views.list_classes, name="class-list"),
    path("classes/new/", views.new_class, name="class-new"),

    path("classes/<str:class_pk>/edit/", views.update_class, name="class-edit"),
    path("classes/<str:class_pk>/delete/", views.delete_class, name="class-edit")
    # path('classes/', classes_views.ClassEntityList.as_view(), name="class-list"),
    # path('classes/<str:class_entity_pk>/', classes_views.ClassEntityDetail.as_view(), name='class-detail'),
	
    # # CLASS STUDENT ROUTES
    # path('class-students/', class_students_views.ClassStudentList.as_view(), name="class-student-list"),
    # path('class-students/<str:class_student_pk>/', class_students_views.ClassStudentDetail.as_view(), name="class-student-detail"),

]
