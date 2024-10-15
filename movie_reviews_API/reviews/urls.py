from django.urls import path
from .views import (
    UserRegistrationView,
    UserUpdateView,
    MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,
    ReviewsListCreateAPIView,
    ReviewsRetrieveUpdateDestroyAPIView,
    ReviewCommentListCreateView,
    ReviewCommentRetrieveUpdateDestroyView,
    ReviewLikeRetrieveUpdateDestroyView,
    ReviewLikeListCreateView,
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

    # comments URLs
    path('reviews/<int:review_id>/comments/', ReviewCommentListCreateView.as_view()),  # List and create comments
    path('reviews/<int:review_id>/comments/<int:pk>/', ReviewCommentRetrieveUpdateDestroyView.as_view()), # Retrieve, update, and delete comments

    # likes URLs
    path('reviews/<int:review_id>/likes/', ReviewLikeListCreateView.as_view()),  # List and create list
    path('reviews/<int:review_id>/likes/<int:pk>/', ReviewLikeRetrieveUpdateDestroyView.as_view()), # Retrieve, update, and delete likes
]
