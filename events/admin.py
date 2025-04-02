from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'artist', 'event_date', 'ticket_price', 'available_tickets')
    search_fields = ('title', 'organizer__username', 'artist__stage_name')
    list_filter = ('event_date',)
