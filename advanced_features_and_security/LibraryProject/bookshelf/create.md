# Create Operation

## Command

```python
from bookshelf.models import Book

# Create and Save a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

