from django.contrib import admin
from .models import Booking, Payment

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'tickets_booked', 'total_price', 'confirmed', 'created_at')
    search_fields = ('user__username', 'event__title')
    list_filter = ('confirmed', 'created_at')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'payment_status', 'transaction_id', 'created_at')
    search_fields = ('booking__user__username', 'transaction_id')
    list_filter = ('payment_status', 'created_at')
