from django.db import models

# Create your models here.
class Shirt(models.Model):
    description = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    purchase_date = models.DateField()
    size = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Dress(models.Model):
    description = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    purchase_date = models.DateField()
    size = models.CharField(max_length=100)
    occasion = models.CharField(max_length=100)

    def __str__(self):
        return self.description