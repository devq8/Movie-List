from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True,)
    watched = models.BooleanField()

    def __str__(self):
        return self.title


class List(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        primary_key = False,
    )
    movies = models.ManyToManyField(
        Movie,
        related_name = "movies",
    )

    def __str__(self):
        return f"{self.user} List"