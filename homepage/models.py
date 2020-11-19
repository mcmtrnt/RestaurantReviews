from django.db import models

# Create your models here.
class Reviews(models.Model):
    restaurant = models.TextField(null=True)
    review = models.TextField(null=True)
