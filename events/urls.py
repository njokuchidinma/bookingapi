from django.urls import path
from .views import EventView



urlpatterns = [
    path('event/', EventView.as_view(), name='events-listed'),
    path('event/<int:pk>/', EventView.as_view(), name='event-detail'),
]