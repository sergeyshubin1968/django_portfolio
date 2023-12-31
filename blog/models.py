from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title
