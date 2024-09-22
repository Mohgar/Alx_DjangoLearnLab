from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet 

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
 
 

 