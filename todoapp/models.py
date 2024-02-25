from django.db import models
from datetime import date
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateField(blank=False, default=date.today)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
