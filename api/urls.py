from django.urls import include, path

from classes import views as classes_views
from .views import views
from .views import user_views
from .views import jwt_views
from .views import school_views
from .views import student_views
from .views import report_views
from .views import schedule_views
from curriculum.views import assessment_views, curriculum_views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'subjects', curriculum_views.SubjectViewSet,
                basename='subject')
router.register(r'levels', curriculum_views.LevelViewSet, basename='level')
# router.register(r'schools/(?P<school_pk>\d+)/subjects', curriculum_views.SubjectViewSet, basename='subject')


urlpatterns = [
    # GREETING ROUTE
    path('', views.helloWorld, name="hello-world"),


    # AUTH ROUTES
    path('token/', jwt_views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # USER ROUTES
    path('users/', user_views.getUsers, name="get-users"),
    path('users/<str:user_pk>/get/',
         user_views.getUserProfileById, name="get-user-profile"),
    path('users/add/', user_views.addUser, name="add-user"),
    path('users/<str:user_pk>/update/',
         user_views.updateUser, name="update-user"),
    path('users/<str:user_pk>/change-password/',
         user_views.changePassword, name="change-password"),


    # TEACHER-USER ROUTES
    path('teachers/', user_views.listTeachers, name="get-users"),
    path('users/teachers/add/', user_views.addTeacher, name="add-teacher"),


    # SCHOOL ROUTES
    path('schools/', school_views.listSchools, name="list-schools"),
    path('schools/<str:school_pk>/get/',
         school_views.getSchoolById, name="get-school-by-id"),
    path('schools/add/', school_views.addSchool, name="add-school"),
    path('schools/<str:school_pk>/update/',
         school_views.updateSchool, name="update-school"),
    path('schools/<str:school_pk>/delete/',
         school_views.deleteSchool, name="delete-school"),

    # SCHOOL DAY ROUTES
    path('schools/<str:school_pk>/days/',
         school_views.SchoolDayList.as_view(), name='school-day-list'),
    path('schools/days/<str:school_day_pk>/',
         school_views.SchoolDayDetail.as_view(), name='school-day-detail'),

    # SCHOOL-USER ROUTES
    path('users/<str:user_pk>/schools/', school_views.listUserSchools,
         name='get-schools-by-user-access'),


    # SCHOOL-TEACHER ROUTES
    path('schools/<str:school_pk>/teachers/',
         user_views.listSchoolTeachers, name="list-school-teachers"),


    # SCHOOL-CLASS ROUTES
    path('schools/<str:school_pk>/classes/',
         classes_views.listSchoolClasses, name="list-school-classes"),
    path('schools/<str:school_pk>/classes/day/<str:day_pk>/',
         classes_views.listSchoolTodayClasses, name='list-school-today-classes'),

    # SCHOOL-STUDENT ROUTES
    path('schools/<str:school_pk>/students/',
         student_views.listSchoolStudents, name="get-students-by-school"),

    # CLASS ROUTES
    path('schools/<str:school_pk>/classes/',
         classes_views.ClassList.as_view(), name="class-list"),
    path('classes/', classes_views.ClassList.as_view(), name="class-list"),
    path('classes/<str:class_pk>/', classes_views.ClassDetail.as_view()),

    # CLASS-TEACHER ROUTES
    path('classes/<str:class_pk>/teachers/add/',
         classes_views.addClassTeacher, name="delete-class-teacher"),
    path('classes/<str:class_pk>/teachers/remove/',
         classes_views.removeClassTeacher, name="delete-class-teacher"),

    # CLASS-STUDENT ROUTES
    path('classes/<str:class_pk>/students/',
         student_views.listClassStudents, name="list-class-students"),
    path('classes/students/add/', classes_views.addClassStudent,
         name='add-class-student'),
    path('classes/<str:class_pk>/students/<str:student_pk>/delete/',
         classes_views.deleteClassStudent, name="delete-class-student"),


    # STUDENT ROUTES
    path('students/', student_views.listStudents, name="get-students"),
    path('students/<str:student_pk>/get/',
         student_views.getStudent, name="get-student"),
    path('students/add/', student_views.addStudent, name="add-student"),
    path('students/<str:student_pk>/update/',
         student_views.updateStudent, name="update-student"),
    path('students/<str:student_pk>/delete/',
         student_views.deleteStudent, name="delete-student"),

    #
    # REPORT ROUTES
    #
    path('reports/', report_views.listReports, name="list-reports"),
    path('classes/<str:class_pk>/reports/date/<str:date_pk>/',
         report_views.getReportByClassAndDate, name="get-report-by-date"),
    path('reports/create/', report_views.createReportAndReportDetails,
         name="create-report"),
    path('reports/<str:pk>/delete/',
         report_views.deleteReport, name="delete-report"),

    # TODO: STUDENT-REPORT ROUTES FOR LATER
    # path('students/<str:student_pk>/reports/', report_views.getTodayReportByStudentId, name="get-today-report-by-student-id"),


    # REPORT DETAILS ROUTES
    path('reports/<str:report_pk>/details/',
         report_views.listReportsDetailsByReportId, name="get-report-details"),
    # path('reports/details/create/', report_views.createReportDetails, name="create-report-details"),
    path('reports/details/<str:detail_pk>/',
         report_views.updateReportDetails, name="delete-report-details"),
    # path('reports/details/<str:detail_pk>/delete/', report_views.deleteReportDetails, name="delete-report-details"),



    # ViewSetRoutes
    path('', include(router.urls)),

    # SCHEDULE ROUTES
    path('weekdays/', schedule_views.getWeekdays, name='weekday'),

    # SUBJECT-LEVEL URI PATHS
    path('subject-levels/', curriculum_views.SubjectLevelList.as_view(),
         name='subjectlevel-list'),
    path('schools/<int:school_pk>/subject-levels/',
         curriculum_views.SubjectLevelList.as_view(), name='school-subjectlevel-list'),
    path('schools/<int:school_pk>/subjects/<int:subject_pk>/levels/',
         curriculum_views.SubjectLevelList.as_view(), name='school-subject-specific-level-list'),
    path('subject-levels/<int:subject_level_pk>/',
         curriculum_views.SubjectLevelDetail.as_view(), name='subjectlevel-detail'),

    # MODULE URI PATHS
    path('modules/', curriculum_views.ModuleList.as_view(), name='list-modules'),
    path('schools/<school_pk>/modules/', curriculum_views.ModuleList.as_view(), name='list-modules'),
    path('modules/<int:module_pk>/', curriculum_views.ModuleDetail.as_view(), name='unit-detail'),
    
    # MODULE-TYPE URI PATHS
    path('module-types/', curriculum_views.ModuleTypeList.as_view(), name='list-module-types'),
    path('schools/<str:school_pk>/module-types/', curriculum_views.ModuleTypeList.as_view(), name='list-module-types'),
    path('module-types/<str:module_type_pk>/', curriculum_views.ModuleTypeDetail.as_view(), name='module-types-detail'),

    # ASSESSMENT-TYPE URI PATHS
    path('assessment-types/', assessment_views.AssessmentTypeList.as_view(), name='assessment-types-list'),

    #  question for Kos

    # is it better to have the hierarchy in the uri?
    # like schools/5/subjects/
    # but what about delete
    # would I do
    # schools/5/subjects/1/delete/
    # schools/5/subjects/1/update/
    # and what about filters
    # would i do schools/5/subjects/?name=Grammar&teacher=Mark&time=night
]
