from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_artist', 'is_event_organizer', 'is_event_promoter', 'is_staff')
    list_filter = ('is_artist', 'is_event_organizer', 'is_event_promoter', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
