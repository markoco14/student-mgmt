from django.urls import include, path

from students.views import student_assessment_views, student_attendance_views, student_views


urlpatterns = [

    # STUDENT ROUTES
    path('students/', student_views.StudentList.as_view(), name='student-list'),
    path('schools/<str:school_pk>/students/',
         student_views.StudentList.as_view(), name='student-list'),
    path('students/<str:student_pk>/',
         student_views.StudentDetail.as_view(), name='student-detail'),

    # STUDENT ATTENDANCE ROUTES
    path('student-attendances/', student_attendance_views.StudentAttendanceList.as_view(),
         name='student-attendance-list'),
    path('schools/<str:school_pk>/student-attendances/',
         student_attendance_views.StudentAttendanceList.as_view(), name='school-student-attendance-list'),
    path('student-attendances/<str:student_attendance_pk>/',
         student_attendance_views.StudentAttendanceDetail.as_view(), name='student-attendance-list'),

		# STUDENT ASSESSMENT ROUTES
    path('student-assessments/', student_assessment_views.StudentAssessmentList.as_view(),
         name='student-assessment-list'),
    path('students/<str:student_pk>/student-assessments/',
         student_assessment_views.StudentAssessmentList.as_view(), name='student-assessment-list'),

]
