from django.db import models

# my models here.


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=75)
    is_done = models.BooleanField()

    def __str__(self):
        return self.name
