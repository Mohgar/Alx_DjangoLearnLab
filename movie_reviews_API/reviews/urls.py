from django.urls import path
from .views import (
    UserRegistrationView,
    UserUpdateView,
    MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,
    ReviewsListCreateAPIView,
    ReviewsRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # User URLs
    path('users/register/', UserRegistrationView.as_view()),  # User registration
    path('users/update/', UserUpdateView.as_view()),  # User update

    # Movie URLs
    path('movies/', MovieListCreateAPIView.as_view()),  # List and create movies
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view()),  # Retrieve, update, and delete movie

    # Review URLs
    path('reviews/', ReviewsListCreateAPIView.as_view()),  # List and create reviews
    path('reviews/<int:pk>/', ReviewsRetrieveUpdateDestroyAPIView.as_view()),  # Retrieve, update, and delete review
]
