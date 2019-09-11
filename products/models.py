from django.db import models

# Create your models here.

class Hearing_aid(models.Model):
    name = models.CharField(max_length=254, default='')
    model_type = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name