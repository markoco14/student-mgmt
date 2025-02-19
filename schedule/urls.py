"""
contain general urls
"""

from django.urls import path

from schedule import views as schedule_views


urlpatterns = [
    # SCHEDULE ROUTES
    path('weekdays/', schedule_views.getWeekdays, name='weekday'),

]
