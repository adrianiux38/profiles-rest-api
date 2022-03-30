from rest_framework import serializers
from profiles_api import models



class MessageSerializer(serializers.Serializer):
    date = serializers.DateTimeField()
    fromName = serializers.CharField(max_length=21)
    _id_ = serializers.CharField(max_length = 23)
    clientPayload = serializers.CharField(allow_blank=True)
    message = serializers.CharField(required=False)
    operatorId = serializers.CharField(max_length = 30, allow_null=True)
    fromCustomer = serializers.BooleanField()


class BotSerializer(serializers.Serializer):
    """Serializes the fields of botmaker requests"""
    lastName = serializers.CharField()
    chatPlatform = serializers.CharField(max_length=30)
    customerCreationTime = serializers.DateTimeField()
    contactId = serializers.CharField(max_length=22)
    sessionId = serializers.CharField()
    type = serializers.CharField(max_length=22)
    whatsappNumber = serializers.CharField(max_length=12)
    firstName = serializers.CharField()
    sessionCreationTime = serializers.DateTimeField()
    v = serializers.CharField(max_length=10)
    customerId = serializers.CharField(max_length=21)
    audio = serializers.CharField(required=False)
    video = serializers.CharField(required=False)
    file = serializers.CharField(required=False)
    image = serializers.CharField(required=False)
    chatChannelId= serializers.CharField()
    messages = MessageSerializer(many=True)
    


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our ApiView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

