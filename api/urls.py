"""
contain general urls
"""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from .views import views
from .views import jwt_views
from .views import schedule_views


urlpatterns = [
    # GREETING ROUTE
    path('', views.helloWorld, name="hello-world"),

    # AUTH ROUTES
    path('token/', jwt_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
         
    # SCHEDULE ROUTES
    path('weekdays/', schedule_views.getWeekdays, name='weekday'),

]
