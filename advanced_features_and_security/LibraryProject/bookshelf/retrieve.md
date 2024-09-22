# Retrieve Operation

## Command

```python
from bookshelf.models import Book

# Retrieve all books
book = Book.objects.get(title="1984")
