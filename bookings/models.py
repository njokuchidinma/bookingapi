from accounts.models import User
from django.db import models
from events.models import Event



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    tickets_booked = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.total_price = self.tickets_booked * self.event.ticket_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"


class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    payment_status = models.CharField(max_length=200, choices=[('PENDING', 'pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')])
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.payment_status}"