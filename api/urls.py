"""
contain general urls
"""

from django.urls import path


from api import views


urlpatterns = [
    # GREETING ROUTE
    path('', views.healthCheck, name="health-check"),
]
