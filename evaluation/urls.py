from django.urls import include, path

from evaluation.views import evaluation_attribute_views, range_attribute_views, text_attribute_views
from evaluation.views import student_evaluation_views


urlpatterns = [
    # EVALUATION ATTRIBUTE ROUTES
    path('evaluation-attributes/', evaluation_attribute_views.EvaluationAttributeList.as_view(),
         name="evaluation-attribute-list"),
    path('schools/<str:school_pk>/evaluation-attributes/',
         evaluation_attribute_views.EvaluationAttributeList.as_view(), name="evaluation-attribute-list"),
    path('evaluation-attributes/<str:evaluation_attribute_pk>/',
         evaluation_attribute_views.EvaluationAttributeDetail.as_view(), name="evaluation-attribute-detail"),

    # RANGE ATTRIBUTE
    path('range-attributes/', range_attribute_views.RangeEvaluationAttributeList.as_view(),
         name="range-attribute-list"),
    path('schools/<str:school_pk>/range-attributes/', range_attribute_views.RangeEvaluationAttributeList.as_view(),
         name="range-attribute-list"),
    path('range-attributes/<str:range_attribute_pk>/',
         range_attribute_views.RangeEvaluationAttributeDetail.as_view(), name="range-attribute-detail"),

    # TEXT ATTRIBUTE
    path('text-attributes/', text_attribute_views.TextEvaluationAttributeList.as_view(),
         name="text-attribute-list"),
    path('schools/<str:school_pk>/text-attributes/',
         text_attribute_views.TextEvaluationAttributeList.as_view(), name="text-attribute-list"),
    path('text-attributes/<str:text_attribute_pk>/',
         text_attribute_views.TextEvaluationAttributeDetail.as_view(), name="text-attribute-detail"),

    # DAILY REPORT PAGE ROUTES ROUTES
    path('schools/<str:school_pk>/daily-report-attributes/',
         evaluation_attribute_views.get_daily_report_eval_attributes, name='daily-report-attribute-list'),

    # STUDENT EVALUATION ROUTES
    path('daily-evaluations/', student_evaluation_views.StudentEvaluationList.as_view(),
         name='daily-evaluation-list'),
    path('students/<str:student_pk>/daily-evaluations/',
         student_evaluation_views.StudentEvaluationList.as_view(), name='daily-evaluation-list'),
    path('schools/<str:school_pk>/daily-evaluations/',
         student_evaluation_views.StudentEvaluationList.as_view(), name='daily-evaluation-list'),

    path('daily-evaluations/<str:student_evaluation_pk>/',
         student_evaluation_views.StudentEvaluationDetail.as_view(), name="daily-evaluation-detail"),

    path('batch-delete-daily-evaluations/<str:student_pk>/',
         student_evaluation_views.batch_delete_evaluations_for_day, name="batch-delete-evaluations"),



]
