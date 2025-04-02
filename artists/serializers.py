from .models import ArtistProfile
from accounts.serializers import UserSerializer
from rest_framework.serializers import ModelSerializer, ValidationError



class ArtistProfileSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ArtistProfile
        fields = ['id', 'user', 'stage_name', 'genre', 'discography', 'bio', 'contact_email', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        if not user or not user.is_authenticated:
            raise ValidationError('Authentication required to create artist profile.')
        if not user.is_artist:
            raise ValidationError('Only users with artist role can create profiles')
        return ArtistProfile.objects.create(user=user, **validated_data)