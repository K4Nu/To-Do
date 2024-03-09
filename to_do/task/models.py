from django.db import models
import datetime

class Task(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_start=models.DateField(default=datetime.date.today)
    date_end=models.DateField(default=datetime.date.today)
    color=models.CharField(max_length=7)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title