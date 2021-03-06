from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max_length = required
    description = models.TextField(blank = True, null = True) #if blank is false that means field is required
    price = models.DecimalField(decimal_places = 2, max_digits = 10000)
    summary = models.TextField()
    featured = models.BooleanField() #null = True, default = True