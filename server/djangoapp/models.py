# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    BRAND_LEVEL = [
        ('BUDGET', 'Budget'),
        ('MEDIUM', 'Medium'),
        ('PREMIUM', 'Premium'),
        ('LUXURY', 'Luxury')
    ]
    brand_level = models.CharField(max_length=10, choices=BRAND_LEVEL, default='MEDIUM')
    
    def __str__(self):
        return self.name  # Return the name as the string representation


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    dealer_id = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('PICKUP', 'Pickup'),
        ('VAN', 'Van'),
        ('MINIVAN', 'Minivan'),
        ('COUPE', 'Coupe'),
        ('CABRIO', 'Cabrio')
    ]
    CAR_FUEL = [
        ('GASOLINE', 'Gasoline'),
        ('DIESEL', 'Diesel'),
        ('LPG', 'LPG'),
        ('HYBRID', 'Hybrid'),
        ('ELECTRIC', 'Electric'),
        ('OTHER', 'Other')
    ]
    CAR_COLOR = [
        ('RED', 'Red'),
        ('ORANGE', 'Orange'),
        ('YELLOW', 'Yellow'),
        ('GREEN', 'Green'),
        ('BLUE', 'Blue'),
        ('PURPLE', 'Purple'),
        ('BROWN', 'Brown'),
        ('GREY', 'Grey'),
        ('WHITE', 'White'),
        ('BLACK', 'Black')
    ]
    CAR_STATUS = [
        ('COMING', 'Coming'),
        ('AVAILABLE', 'Available'),
        ('RESERVED', 'Reserved'),
        ('SOLD', 'Sold')
    ]
    status = models.CharField(max_length=10, choices=CAR_STATUS, default='COMING')
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ])
    fuel = models.CharField(max_length=10, choices=CAR_FUEL, default='GASOLINE')
    engine = models.FloatField(default=2.0,
        validators=[
            MaxValueValidator(10.0),
            MinValueValidator(0.5)
        ])
    color = models.CharField(max_length=10, choices=CAR_COLOR, default='WHITE')

    def __str__(self):
        return self.name  # Return the name as the string representation