from django.db import models

# Create your models here.
class Entry(models.Model):
    """This is the default entry model"""
    entry_type = models.CharField(max_length=50)
    description = models.CharField(max_length=120)
    category = models.CharField(max_length=60)
    date = models.DateField()
    amount = models.DecimalField(max_digits=100, decimal_places=2)

