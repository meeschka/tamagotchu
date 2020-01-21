from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name