from django.urls import path, include
from .views import add_book
urlpatterns = [
    path('create_book', add_book, name='create_book' )
]
