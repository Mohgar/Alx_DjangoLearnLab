from rest_framework import serializers
from .models import Movie, Reviews



class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date']
        extra_kwargs = {
            'title': {'required': True},  # Movie Title required
            'description': {'required': False},  # Description is optional
            'release_date': {'required': True},  # Make Release Date required
        }


class ReviewsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['movie_title', 'user_id', 'rating', 'review_content', 'created_date' ]
        read_only_fields = ['created_date']
        extra_kwargs = {
            'movie_title': {'required': True},  # Movie Title required
            'review_content': {'required': True},  # Review Content required
        }

    def validate_rating(self, data):
        if data['rating'] < 1 or data['rating'] > 5 :
            raise serializers.ValidationError(" rating must between 1 and 5")

        return data





