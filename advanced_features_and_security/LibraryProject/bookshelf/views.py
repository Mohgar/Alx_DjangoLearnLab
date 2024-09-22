from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book
from .models import CustomUser
from .forms import ExampleForm


# Django ORM is used to safely retrieve all books, preventing SQL injection
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books':books})

# Validate user input using ExampleForm to prevent malicious data entry
@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExampleForm()

    return render(request, 'form_example.html', {'form': form})


@permission_required("bookshelf.can_view", raise_exception=True)
def view_books(request):
    return render(request, 'all_books.html')


@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_books(request):
    return render(request, 'delete_books.html')
