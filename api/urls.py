"""
contain general urls
"""

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from .views import views
from .authentication import views as auth_views
from schedule import views as schedule_views


urlpatterns = [
    # GREETING ROUTE
    path('', views.healthCheck, name="health-check"),

    # AUTH ROUTES
    path('token/', auth_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
         
    # SCHEDULE ROUTES
    path('weekdays/', schedule_views.getWeekdays, name='weekday'),

]
