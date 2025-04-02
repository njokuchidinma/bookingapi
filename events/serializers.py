from .models import Event
from accounts.serializers import UserSerializer
from artists.serializers import ArtistProfileSerializer
from rest_framework.serializers import ModelSerializer, ValidationError


class EventSerializer(ModelSerializer):
    artist = ArtistProfileSerializer(read_only=True)
    organizer = UserSerializer(read_only=True)
    promoter = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            'id', 'organizer', 'promoter', 'artist', 'title', 'description', 
            'location', 'event_date', 'ticket_price', 'available_tickets', 'created_at'
        ]
        read_only_fields = ['organizer']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        if not user or not user.is_event_organizer:
            raise ValidationError('Only event organizers can create an event.')

        # Get artist and promoter IDs from the request
        artist_id = request.data.get('artist')
        promoter_id = request.data.get('promoter')

        from artists.models import ArtistProfile
        from accounts.models import User as AccountUser

        if not artist_id:
            raise ValidationError('Artist ID is required.')

        try:
            artist = ArtistProfile.objects.get(id=artist_id)
        except ArtistProfile.DoesNotExist:
            raise ValidationError('Artist not found.')

        promoter = None
        if promoter_id:
            try:
                promoter = AccountUser.objects.get(id=promoter_id)
            except AccountUser.DoesNotExist:
                raise ValidationError('Promoter not found.')

        return Event.objects.create(
            organizer=user,
            artist=artist,
            promoter=promoter,
            **validated_data
        )

    def update(self, instance, validated_data):
        request = self.context.get('request')

        artist_id = request.data.get('artist')
        promoter_id = request.data.get('promoter')

        from artists.models import ArtistProfile
        from accounts.models import User as AccountUser

        if artist_id:
            try:
                instance.artist = ArtistProfile.objects.get(id=artist_id)
            except ArtistProfile.DoesNotExist:
                raise ValidationError('Artist not found.')

        if promoter_id:
            try:
                instance.promoter = AccountUser.objects.get(id=promoter_id)
            except AccountUser.DoesNotExist:
                raise ValidationError('Promoter not found.')

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

