from django.urls import include, path

from students.views import student_assessment_views, student_attendance_views, student_views


urlpatterns = [

    # STUDENT ROUTES
    path('students/', student_views.StudentList.as_view(), name='student-list'),
    path('schools/<str:school_pk>/students/',
         student_views.StudentList.as_view(), name='student-list'),
    path('students/<str:student_pk>/',
         student_views.StudentDetail.as_view(), name='student-detail'),

	# STUDENTS WITH ATTENDANCE RECORDS
	path('students-with-attendance/', student_attendance_views.get_students_with_attendance, name='student-with-attendance-list'),
	
	# STUDENTS WITH EVALUATION RECORDS
	path('students-with-evaluations/', student_views.get_students_with_evaluations, name='student-with-evaluations-list'),

	path('create-student-evaluations/', student_views.create_evaluation_records_for_class_list, name='batch-create-evaluations'),

    # STUDENT ATTENDANCE ROUTES
    path('student-attendances/', student_attendance_views.StudentAttendanceList.as_view(),
         name='student-attendance-list'),
    path('student-attendances/<str:student_attendance_pk>/',
         student_attendance_views.StudentAttendanceDetail.as_view(), name='student-attendance-list'),

    # ATTENDANCE FOR EVALUATIONS PAGE
    path('students-here-today/', student_attendance_views.get_students_here_today,
         name='student-today-list'),

    # BATCH MAKE STUDENT ATTENDANCE
    path('batch-student-attendances/', student_attendance_views.create_attendance_records_for_class_list,
         name='batch-student-attendance-list'),

    # STUDENT ASSESSMENT ROUTES
    path('student-assessments/', student_assessment_views.StudentAssessmentList.as_view(),
         name='student-assessment-list'),
    path('students/<str:student_pk>/student-assessments/',
         student_assessment_views.StudentAssessmentList.as_view(), name='student-assessment-list'),

]
