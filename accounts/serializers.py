from .models import User
from rest_framework.serializers import ModelSerializer, CharField, EmailField, ValidationError


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)  # ✅ Ensure password is captured

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_artist', 'is_event_organizer', 'is_event_promoter')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # 🔐 hashes the password
        user.save()
        return user



class ChangePasswordSerializer(ModelSerializer):
    old_password = CharField(required=True, write_only=True)
    new_password = CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password']

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise ValidationError("Old password is incorrect.")
        return value
    
    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance