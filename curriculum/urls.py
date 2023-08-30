from django.urls import path
from curriculum.views import assessment_views, curriculum_views



urlpatterns = [
    
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
    path('assessment-types/', assessment_views.AssessmentTypeList.as_view(), name='assessment-type-list'),
    path('schools/<str:school_pk>/assessment-types/', assessment_views.AssessmentTypeList.as_view(), name='assessment-type-list'),
    path('assessment-types/<str:assessment_type_pk>/', assessment_views.AssessmentTypeDetail.as_view(), name='assessment-type-detail'),


    # ASSESSMENT URI PATHS
    path('assessments/', assessment_views.AssessmentList.as_view(), name='assessment-list'),
    path('schools/<str:school_pk>/assessments/', assessment_views.AssessmentList.as_view(), name='assessment-list'),
    path('assessments/<str:assessment_pk>/', assessment_views.AssessmentDetail.as_view(), name='assessment-list'),
]
