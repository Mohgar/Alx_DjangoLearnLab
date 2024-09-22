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
        user = get_user_model()(**validated_data)
        user.set_password(validated_data['password'])  
        user.save()

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


