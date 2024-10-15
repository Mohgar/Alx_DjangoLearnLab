from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie, Reviews, ReviewLike, ReviewComment



# Serializer for User Registration
# This serializer handles the creation of a new user, including validation and password hashing.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specify the User model for this serializer
        fields = ['id', 'username', 'email', 'password']  # Fields to be included in serialization
        extra_kwargs = {
            'password': {'write_only': True},  # Password should be write-only to protect user privacy
        }

    def create(self, validated_data):
        # Create a new user instance with validated data
        user = User(**validated_data)  # Unpack validated data into User model fields
        user.set_password(validated_data['password'])  # Hash the password for security
        user.save()  # Save the new user instance to the database
        return user  # Return the newly created user instance


# Serializer for User Update
# This serializer allows existing users to update their username, email, and password.
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specify the User model for this serializer
        fields = ['username', 'email', 'password']  # Fields available for updating
        extra_kwargs = {
            'password': {'write_only': True},  # Password should remain write-only for security
        }

    def update(self, instance, validated_data):
        # Update the existing user instance with new data from validated_data
        instance.username = validated_data.get('username', instance.username)  # Update username if provided
        instance.email = validated_data.get('email', instance.email)  # Update email if provided

        # If a new password is provided, hash it and update the user instance
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])  # Hash the new password

        instance.save()  # Save the updated user instance to the database
        return instance  # Return the updated user instance


# Serializer for the Movie model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  # Specify the model associated with this serializer
        fields = ['id', 'title', 'description', 'release_date','user']
        extra_kwargs = {
            'title': {'required': True},         # Movie Title required
            'description': {'required': False},  # Description is optional
            'release_date': {'required': True},  # Release Date required
        }

# Serializer for the Reviews model
class ReviewsSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie_title.title')  # Get the title from the related movie

    class Meta:
        model = Reviews  # Specify the model associated with this serializer
        fields = ['id', 'movie_title', 'user', 'rating', 'review_content', 'created_date' ]
        read_only_fields = ['created_date']  # Prevent modification of created_date by users
        extra_kwargs = {
            'movie_title': {'required': True},     # Movie Title required
            'review_content': {'required': True},  # Review Content required
        }

    def validate_rating(self, data):
        if data['rating'] < 1 or data['rating'] > 5 :
            # Raise an error if rating is out of range
            raise serializers.ValidationError(" rating must be between 1 and 5")

        return data  # Return the validated rating

# Serializer for the ReviewLike model
class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike  # Specify the model associated with this serializer
        fields = ['id', 'review', 'user']

# Serializer for the ReviewComment model
class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment  # Specify the model associated with this serializer
        fields = ['id', 'review', 'user', 'comment_content', 'created_date']




