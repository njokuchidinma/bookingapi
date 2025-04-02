from .views import ArtistProfileView
from django.urls import path



urlpatterns = [
    path('profiles/', ArtistProfileView.as_view(), name='artist-profile'),
    path('profiles/<int:pk>/', ArtistProfileView.as_view(), name='artist-profile-detail'),
]