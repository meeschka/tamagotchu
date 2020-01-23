from django.db import models
from django.urls import reverse
from datetime import date


MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.color} {self.name}"

    def get_absolute_url(self):
        return reverse("toys_detail", kwargs={"pk": self.pk})
    
class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    age = models.PositiveIntegerField(default=0)
    toys = models.ManyToManyField(Toy)

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

class PetPhoto(models.Model):
    url = models.CharField(max_length=200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    s3key = models.CharField(max_length=200)
    def __str__(self):
        return f"The photo url for pet {self.pet_id} is at {self.url}"

class ToyPhoto(models.Model):
    url = models.CharField(max_length=200)
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    s3key = models.CharField(max_length=200)
    def __str__(self):
        return f"The photo url for toy {self.toy_id} is at {self.url}"
