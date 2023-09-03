from django.urls import include, path

from classes import views as classes_views

urlpatterns = [
		# CLASS ROUTES
    path('schools/<str:school_pk>/classes/',
         classes_views.ClassEntityList.as_view(), name="class-list"),
    path('classes/', classes_views.ClassEntityList.as_view(), name="class-list"),
    path('classes/<str:class_pk>/', classes_views.ClassEntityDetail.as_view()),

		# ROUTES NOT REALLY NECESSARY... A FRONTEND ADAPTER METHOD COULD BE USED INSTEAD..
		# JUST UPDATE THE CLASS WITH THE NORMAL ROUTE, USE PATCH, AND ONLY SEND TEACHER
    # CLASS-TEACHER ROUTES
		# TODO: REMOVE
    path('classes/<str:class_pk>/teachers/add/',
         classes_views.addClassTeacher, name="delete-class-teacher"),
    path('classes/<str:class_pk>/teachers/remove/',
         classes_views.removeClassTeacher, name="delete-class-teacher"),

		#WORKS
    path('classes/students/add/', classes_views.addClassStudent,
         name='add-class-student'),
		# TODO: CHANGE TO class-students/
    path('classes/<str:class_pk>/students/<str:student_pk>/delete/',
         classes_views.deleteClassStudent, name="delete-class-student"),

		 # SCHOOL-CLASS ROUTES
#     path('schools/<str:school_pk>/classes/',
#          classes_views.listSchoolClasses, name="list-school-classes"),
#     path('schools/<str:school_pk>/classes/day/<str:day_pk>/',
#          classes_views.listSchoolTodayClasses, name='list-school-today-classes'),
]