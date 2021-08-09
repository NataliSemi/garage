from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
app_name = 'app'

urlpatterns = [
    #path('login/', LoginAPIView.as_view(), name='login'),
    path('login/', views.LoginAPIView.as_view(), name="login_view"),

]
