from django.urls import path
from curriculum.views import assessment_views, curriculum_views, level_views, old_subject_views, subject_level_views, subject_views
from curriculum.views import level_views



urlpatterns = [

	# SUBJECT URI PATHS
	path('subjects/', subject_views.list_subjects, name="subject-list"),
	path('subjects/new/', subject_views.new_subject, name="subject-new"),
	path('subjects/<str:subject_pk>/', subject_views.show_subject, name="subject-detail"),
	path('subjects/<str:subject_pk>/edit/', subject_views.edit_subject, name="subject-edit"),
	
    # LEVEL URI PATHS
    path('levels/', level_views.list_levels, name='level-list'),
    path('levels/new/', level_views.new_level, name="level-new"),
	path('levels/<str:level_pk>/', level_views.show_level, name='level-detail'),
	path('levels/<str:level_pk>/edit', level_views.edit_level, name='level-update'),
	path('levels/<str:level_pk>/delete', level_views.delete_level, name='level-delete'),
    
    # SUBJECT-LEVEL URI PATHS
    # path('subject-levels/', subject_level_views.SubjectLevelList.as_view(),
    #      name='subject-level-list'),
    # path('subject-levels/<int:subject_level_pk>/',
    #      subject_level_views.SubjectLevelDetail.as_view(), name='subject-level-detail'),
]