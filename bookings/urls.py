from .views import BookingView
from django.urls import path


urlpatterns = [
    path('booking/', BookingView.as_view(), name='booking-list'),
    path('booking/<int:pk>/', BookingView.as_view(), name='booking-detail'),
]