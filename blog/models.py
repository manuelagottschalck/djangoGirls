from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Model representing a blog post."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Method to publish the post by setting the published_date to the current time."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """String representation of the Post model, returning the title."""
        return self.title