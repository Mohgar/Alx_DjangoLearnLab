from django.urls import path
from .views import (
MovieListCreateAPIView,
MovieRetrieveUpdateDestroyAPIView,
ReviewsListCreateAPIView,
ReviewsRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('movie/',MovieListCreateAPIView.as_view() ),
    path('movie/<int:pk>',MovieRetrieveUpdateDestroyAPIView.as_view() ),
    path('reviews/',ReviewsListCreateAPIView.as_view() ),
    path('reviews/<int:pk>',ReviewsRetrieveUpdateDestroyAPIView.as_view() ),

]