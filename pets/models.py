from django.db import models
from django.urls import reverse
from datetime import date


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', kwargs={'pet_id' : self.id})

    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count()>=len(MEALS)

class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(
        max_length = 1,
        choices = MEALS,
        default = MEALS[0][0]
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']