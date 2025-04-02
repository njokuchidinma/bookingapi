from accounts.models import User
from artists.models import ArtistProfile
from django.db import models




class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organized_events')
    promoter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='promoted_events', null=True)
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    available_tickets = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title