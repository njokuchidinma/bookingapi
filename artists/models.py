from accounts.models import User
from django.db import models



class ArtistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist_profile')
    stage_name = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    discography = models.TextField(blank=True, null=True)
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stage_name