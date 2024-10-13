from .serializers import (
    MovieSerializer,
    ReviewsSerializer,
    UserSerializer,
    UserUpdateSerializer
)
from django.contrib.auth.models import User
from .models import Movie, Reviews
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError

# User Registration View
# This view handles user registration, allowing any user to create a new account.
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()  # Queryset for retrieving User objects
    serializer_class = UserSerializer  # Serializer to validate and save user data
    permission_classes = [AllowAny]  # Allow any user to register

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)  # Call the parent class's create method
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# User Update View
# This view allows authenticated users to update their profile information.
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()  # Queryset for retrieving User objects
    serializer_class = UserUpdateSerializer  # Serializer for updating user data
    permission_classes = [IsAuthenticated]  # Only authenticated users can update their info

    def get_object(self):
        # Ensure that users can only update their own profile
        return self.request.user  # Returns the current logged-in user

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)  # Call the parent class's update method
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


# Movie List and Create View
# This view allows authenticated users to list all movies and create new movies.
class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()  # Queryset for retrieving Movie objects
    serializer_class = MovieSerializer  # Serializer for validating and saving movie data
    authentication_classes = [TokenAuthentication]  # Use token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    filter_backends = [filters.SearchFilter]  # Enable search filtering
    search_fields = ['title', 'release_date']  # Fields to search on

    def perform_create(self, serializer):
        # Save the movie instance with the current user as the creator
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)  # Call the parent class's list method
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Movie Retrieve, Update, and Destroy View
# This view allows authenticated users to retrieve, update, or delete a specific movie.
class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()  # Queryset for retrieving Movie objects
    serializer_class = MovieSerializer  # Serializer for validating and saving movie data
    authentication_classes = [TokenAuthentication]  # Use token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    filter_backends = [filters.SearchFilter]  # Enable search filtering
    search_fields = ['title', 'release_date']  # Fields to search on

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)  # Call the parent class's retrieve method
        except NotFound:
            return Response({'error': 'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)  # Call the parent class's update method
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)  # Call the parent class's destroy method
        except NotFound:
            return Response({'error': 'Movie not found.'}, status=status.HTTP_404_NOT_FOUND)


# Reviews List and Create View
# This view allows authenticated users to list all reviews and create new reviews.
class ReviewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()  # Queryset for retrieving Review objects
    serializer_class = ReviewsSerializer  # Serializer for validating and saving review data
    authentication_classes = [TokenAuthentication]  # Use token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    filter_backends = [filters.SearchFilter]  # Enable search filtering
    search_fields = ['movie_title', 'rating']  # Fields to search on


# Reviews Retrieve, Update, and Destroy View
# This view allows authenticated users to retrieve, update, or delete a specific review.
class ReviewsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()  # Queryset for retrieving Review objects
    serializer_class = ReviewsSerializer  # Serializer for validating and saving review data
    authentication_classes = [TokenAuthentication]  # Use token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    filter_backends = [filters.SearchFilter]  # Enable search filtering
    search_fields = ['movie_title', 'rating']  # Fields to search on

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)  # Call the parent class's retrieve method
        except NotFound:
            return Response({'error': 'Review not found.'}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)  # Call the parent class's update method
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)  # Call the parent class's destroy method
        except NotFound:
            return Response({'error': 'Review not found.'}, status=status.HTTP_404_NOT_FOUND)
