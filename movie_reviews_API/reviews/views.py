from .serializers import (
    MovieSerializer,
    ReviewsSerializer,
    UserSerializer,
    UserUpdateSerializer,
    ReviewLikeSerializer,
    ReviewCommentSerializer
)
from django.contrib.auth.models import User
from .models import Movie, Reviews,ReviewLike, ReviewComment
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
    authentication_classes = [TokenAuthentication]  # Use token-based authentication
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


class ReviewLikeListCreateView(generics.ListCreateAPIView):
    # Define the view for listing and creating likes for reviews
    queryset = ReviewLike.objects.all()  # Queryset to retrieve all ReviewLike instances
    serializer_class = ReviewLikeSerializer  # Serializer for validating and serializing the like data
    authentication_classes = [TokenAuthentication]  # Require token authentication for this view
    permission_classes = [IsAuthenticated]  # Only allow access to authenticated users

    def perform_create(self, serializer):
        # Override the perform_create method to customize the behavior of creating a like
        review_id = self.request.data.get('review')  # Get the review ID from the incoming request data

        # Check if the user already liked the review
        if ReviewLike.objects.filter(review_id=review_id, user=self.request.user).exists():
            # If the user has already liked the review, return an error response
            return Response({'detail': 'You have already liked this review.'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the like instance with the current user
        serializer.save(user=self.request.user)  # Save the like and associate it with the authenticated user


class ReviewLikeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # Define the view for retrieving, updating, and deleting a specific like
    queryset = ReviewLike.objects.all()  # Queryset to retrieve all ReviewLike instances
    serializer_class = ReviewLikeSerializer  # Serializer for validating and serializing the like data
    permission_classes = [IsAuthenticated]  # Only allow access to authenticated users
    authentication_classes = [TokenAuthentication]  # Require token authentication for this view

    def get_object(self):
        # Override the get_object method to add custom permission checks
        obj = super().get_object()  # Retrieve the like object using the parent class method
        # Ensure that the requesting user is the owner of the like
        if obj.user != self.request.user:
            # If the user is not the owner, raise a permission denied error
            raise PermissionDenied("You do not have permission to access this like.")
        return obj  # Return the like object if the user is authorized


class ReviewCommentListCreateView(generics.ListCreateAPIView):
    # Define the view for listing and creating comments for reviews
    queryset = ReviewComment.objects.all()  # Queryset to retrieve all ReviewComment instances
    serializer_class = ReviewCommentSerializer  # Serializer for validating and serializing the comment data
    permission_classes = [IsAuthenticated]  # Only allow access to authenticated users
    authentication_classes = [TokenAuthentication]  # Require token authentication for this view

    def perform_create(self, serializer):
        # Override the perform_create method to customize the behavior of creating a comment
        review_id = self.kwargs.get('review_id')  # Get the review ID from the URL parameters
        # Save the comment instance with the current user and the associated review ID
        serializer.save(user=self.request.user, review_id=review_id)  # Automatically set user and review


class ReviewCommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    # Define the view for retrieving, updating, and deleting a specific comment
    queryset = ReviewComment.objects.all()  # Queryset to retrieve all ReviewComment instances
    serializer_class = ReviewCommentSerializer  # Serializer for validating and serializing the comment data
    permission_classes = [IsAuthenticated]  # Only allow access to authenticated users
    authentication_classes = [TokenAuthentication]  # Require token authentication for this view

    def get_object(self):
        # Override the get_object method to add custom permission checks
        obj = super().get_object()  # Retrieve the comment object using the parent class method
        # Ensure that the requesting user is the owner of the comment
        if obj.user != self.request.user:
            # If the user is not the owner, raise a permission denied error
            raise PermissionDenied("You do not have permission to access this comment.")
        return obj  # Return the comment object if the user is authorized


