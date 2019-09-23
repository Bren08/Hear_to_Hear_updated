from django.db import models

# Create your models here.

class Aid(models.Model): 
    brand = models.CharField(max_length=254, default='')
    model_type = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.brand


class Product_Addon(models.Model):
    brand = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    isAccessory = models.BooleanField(default=False)

    def __str__(self):
        return self.brand