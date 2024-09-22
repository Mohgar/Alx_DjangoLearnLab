from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(  # Use create_user method
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],  # Password is hashed
            bio=validated_data.get('bio', ''),  # Use .get() to avoid KeyError
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user


