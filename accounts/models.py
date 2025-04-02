from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='username',
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
    )
    is_artist = models.BooleanField(default=False)
    is_event_organizer = models.BooleanField(default=False)
    is_event_promoter = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username

    @property
    def role(self):
        if self.is_artist:
            return "Artist"
        if self.is_event_organizer:
            return "Organizer"
        if self.is_event_promoter:
            return "Promoter"
        return "User"
