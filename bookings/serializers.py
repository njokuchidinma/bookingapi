from .models import Booking
from accounts.serializers import UserSerializer
from events.serializers import EventSerializer
from rest_framework.serializers import ModelSerializer, ValidationError



class BookingSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    event = EventSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'event', 'tickets_booked', 'total_price', 'created_at', 'confirmed']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        event_id = request.data.get('event')  # get event ID from request body

        if not event_id:
            raise ValidationError("Event ID is required.")

        from events.models import Event  # import here to avoid circular import
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            raise ValidationError("Event not found.")

        if validated_data['tickets_booked'] > event.available_tickets:
            raise ValidationError('Not enough tickets available.')

        event.available_tickets -= validated_data['tickets_booked']
        event.save()

        return Booking.objects.create(user=user, event=event, **validated_data)

