from django.urls import include, path

from assessment.views import assessment_views




# path('students/', student_views.StudentList.as_view(), name='student-list'),
urlpatterns = [
	path('assessments/', assessment_views.AssessmentList.as_view(), name='assessment-list'),
]