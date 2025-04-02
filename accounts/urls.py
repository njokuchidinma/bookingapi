from .views import UserRegistrationView, LoginView, ChangePasswordView
from django.urls import path





urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register-user'),
    path('login/', LoginView.as_view(), name='login-user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]