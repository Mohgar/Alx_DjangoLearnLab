from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Model representing a Movie
class Movie(models.Model):
    title = models.CharField(max_length=255)  # Title of the movie
    description = models.TextField()  # Detailed description of the movie
    release_date = models.DateField()  # Release date of the movie
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # User who added the movie

    def __str__(self):
        return self.title  # Returns the title of the movie when the object is printed


# Model representing Reviews for a Movie
class Reviews(models.Model):
    movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')  # Link to the Movie
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who wrote the review
    rating = models.PositiveIntegerField(blank=False, null=False)  # Rating given by the user (e.g., 1-5)
    review_content = models.TextField(blank=False, null=False)  # Content of the review
    created_date = models.DateTimeField(auto_now_add=True)  # Date when the review was created
    likes_count = models.PositiveIntegerField(default=0) # Track the number of likes

    class Meta:
        # Prevent duplicate reviews from the same user for the same movie
        unique_together = ('movie_title', 'user')
        # Always order reviews by creation date, most recent first
        ordering = ['-created_date']

    def __str__(self):
        # Returns a string representation of the review, including user and movie title and rating
        return f"Review by {self.user.username} for {self.movie_title.title}: {self.rating} stars"

# Model to track which users liked which reviews
class ReviewLike(models.Model):
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)  # review which been liked
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who like the review

    class Meta:
        unique_together = ('review', 'user')  # Prevent multiple likes from the same user

    def __str__(self):
        # Returns a string representation of the likes, including user and movie title
        return f"{self.user.username} liked review for movie: {self.review.movie_title}"

class ReviewComment(models.Model):

    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)  # review which been commented
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user who will comment
    comment_content = models.TextField()  #content of the the comment
    created_date = models.DateTimeField(auto_now_add=True)  # Date when the comment was created

    class Meta:
        # Ordering comments by creation date, with the most recent first
        ordering = ['-created_date']

    def __str__(self):
        # String representation of the comment, showing the username and review ID
        return f"Comment by {self.user.username} on review of the movie: {self.review.movie_title}"


# Signal to create a Token for a new User
@receiver(post_save, sender=User)
def TokenCreate(sender, instance, created, **kwargs):
    # Check if a new user instance was created
    if created:
        Token.objects.create(user=instance)  # Create a token for the newly registered user






