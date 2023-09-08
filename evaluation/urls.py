from django.urls import include, path

from evaluation.views.evaluation_attribute_views import get_daily_report_eval_attributes
from evaluation.views import student_evaluation_views


urlpatterns = [
    # STUDENT ROUTES
    path('schools/<str:school_pk>/daily-report-attributes/', get_daily_report_eval_attributes, name='daily-report-attribute-list'),

    # STUDENT EVALUATION ROUTES
    path('daily-evaluations/', student_evaluation_views.StudentEvaluationList.as_view(), name='daily-evaluation-list'),
    path('students/<str:student_pk>/daily-evaluations/', student_evaluation_views.StudentEvaluationList.as_view(), name='daily-evaluation-list'),
    path('schools/<str:school_pk>/daily-evaluations/', student_evaluation_views.StudentEvaluationList.as_view(), name='daily-evaluation-list'),
]


#  path('users/<str:user_pk>/get/',
#          user_views.getUserProfileById, name="get-user-profile"),