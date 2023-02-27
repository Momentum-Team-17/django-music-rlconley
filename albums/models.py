from django.db import models

# Create your models here.


class Album(models.Model):
    # our Album class is inheriting from Django's
    # Model class, located in models/
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
