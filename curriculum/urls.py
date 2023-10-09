from django.urls import path
from curriculum.views import assessment_views, curriculum_views, level_views, subject_views, subject_level_views



urlpatterns = [

	# SUBJECT URI PATHS
	path('subjects/', subject_views.SubjectList.as_view(), name="subject-list"),
	path('subjects/<str:subject_pk>/', subject_views.SubjectDetail.as_view(), name="subject-detail"),
	
    # LEVEL URI PATHS
    path('levels/', level_views.LevelList.as_view(), name='level-list'),
	path('levels/<str:level_pk>/', level_views.LevelDetail.as_view(), name='level-detail'),
    
    # SUBJECT-LEVEL URI PATHS
    path('subject-levels/', subject_level_views.SubjectLevelList.as_view(),
         name='subject-level-list'),
    path('subject-levels/<int:subject_level_pk>/',
         subject_level_views.SubjectLevelDetail.as_view(), name='subject-level-detail'),
    
		 # MODULE URI PATHS
    path('modules/', curriculum_views.ModuleList.as_view(), name='list-modules'),
    path('modules/<int:module_pk>/', curriculum_views.ModuleDetail.as_view(), name='unit-detail'),
    
    # MODULE-TYPE URI PATHS
    path('module-types/', curriculum_views.ModuleTypeList.as_view(), name='list-module-types'),
    path('schools/<str:school_pk>/module-types/', curriculum_views.ModuleTypeList.as_view(), name='list-module-types'),
    path('module-types/<str:module_type_pk>/', curriculum_views.ModuleTypeDetail.as_view(), name='module-types-detail'),

    # ASSESSMENT-TYPE URI PATHS
#     path('assessment-types/', assessment_views.AssessmentTypeList.as_view(), name='assessment-type-list'),
#     path('schools/<str:school_pk>/assessment-types/', assessment_views.AssessmentTypeList.as_view(), name='assessment-type-list'),
#     path('assessment-types/<str:assessment_type_pk>/', assessment_views.AssessmentTypeDetail.as_view(), name='assessment-type-detail'),


    # ASSESSMENT URI PATHS
#     path('assessments/', assessment_views.AssessmentList.as_view(), name='assessment-list'),
#     path('schools/<str:school_pk>/assessments/', assessment_views.AssessmentList.as_view(), name='assessment-list'),
#     path('assessments/<str:assessment_pk>/', assessment_views.AssessmentDetail.as_view(), name='assessment-list'),

    # MODULE-ASSESSMENT URI PATH
#     path('schools/<str:school_pk>/module-assessments/', assessment_views.module_assessment_page_list, name='assessment-list'),
]
