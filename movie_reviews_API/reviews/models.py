from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Reviews(models.Model):
    movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(blank= False, null= False)
    review_content = models.TextField(blank= False, null= False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.movie.title}"



