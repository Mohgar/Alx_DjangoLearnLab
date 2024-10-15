from django.contrib import admin
from .models import Movie, Reviews, ReviewLike, ReviewComment

admin.site.register(Movie)
admin.site.register(Reviews)
admin.site.register(ReviewLike)
admin.site.register(ReviewComment)

# Register your models here.
