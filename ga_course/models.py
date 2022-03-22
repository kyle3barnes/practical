from django.db import models


# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=128, unique=True)
    start = models.DateField()
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.title
