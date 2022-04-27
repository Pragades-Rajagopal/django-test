from datetime import datetime
from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
 
class Showroom(models.Model):
    showroom_name = models.CharField(max_length=400)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.showroom_name

rating_values = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    price = models.CharField(max_length=12)
    ratings = models.CharField(max_length=1, choices=rating_values)
    brand = models.CharField(max_length=100)
    model_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1980),
            MaxValueValidator(datetime.now().year)
        ],
        help_text="Please use the following format for year of Car model <YYYY>"
    )
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name
