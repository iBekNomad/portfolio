from django.db import models
from datetime import date

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title
