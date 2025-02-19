"""
contain general urls
"""

from django.urls import path


from api import views

from schedule import views as schedule_views


urlpatterns = [
    # GREETING ROUTE
    path('', views.healthCheck, name="health-check"),

 
    # SCHEDULE ROUTES
    path('weekdays/', schedule_views.getWeekdays, name='weekday'),

]
