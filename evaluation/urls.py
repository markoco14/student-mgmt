from django.urls import include, path

from evaluation.views import get_daily_report_eval_attributes


urlpatterns = [
    # STUDENT ROUTES
    path('schools/<str:school_pk>/daily-report-attributes/', get_daily_report_eval_attributes, name='daily-report-attribute-list'),
]


#  path('users/<str:user_pk>/get/',
#          user_views.getUserProfileById, name="get-user-profile"),