from django.urls import include, path

from classes.views import class_assessment_views, classes_views, class_students_views

urlpatterns = [
    # CLASS ROUTES
    path('classes/', classes_views.ClassEntityList.as_view(), name="class-list"),
    path('classes/<str:class_entity_pk>/', classes_views.ClassEntityDetail.as_view(), name='class-detail'),
	
    # CLASS STUDENT ROUTES
    path('class-students/', class_students_views.ClassStudentList.as_view(), name="class-student-list"),
    path('class-students/<str:class_student_pk>/', class_students_views.ClassStudentDetail.as_view(), name="class-student-detail"),

    # CLASs ASSESSMENT ROUTES
    path('class-assessments/', class_assessment_views.ClassAssessmentList.as_view(),
         name='student-assessment-list'),
    path('classes/<str:class_pk>/class-assessments/',
         class_assessment_views.ClassAssessmentList.as_view(), name='class-assessment-list'),

]
