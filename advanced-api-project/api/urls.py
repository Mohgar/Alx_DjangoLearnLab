from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView,  BookUpdateView, BookDeleteView
urlpatterns = [
    path('books/',BookListView.as_view(),name= "booklist" ),
    path('books/<int:pk>/',BookDetailView.as_view(),name= "bookdetail" ),
    path('books/create/',BookCreateView.as_view(),name= "bookcreate" ),
    path('books/update/<int:pk>',BookUpdateView.as_view(),name= "bookupdate" ),
    path('books/delete/<int:pk>',BookDeleteView.as_view(),name= "bookdelete" )



]