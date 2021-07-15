from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=64, null=False)
    company = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, related_name='cars', on_delete=CASCADE)
    make = models.CharField(max_length=64, null=False)
    model = models.CharField(max_length=64, null=False)
    year = models.IntegerField(null=False)
    color = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"