from django.db import models
from django.urls import reverse
from django import forms


# choice variables
ENTRY_TYPE_CHOICES = [
    ("Income", "Income"),
    ("Expense", "Expense")
]

CATEGORY_CHOICES = [
    # expense categories
    ("food","Food"),
    ("housing","Housing"), 
    ("transportation","Transportation"),
    ("fun & entertainment", "Fun & Entertainment"),
    ("investing", "Investing"),
    ("interest & debts", "Interest & Debts"),
    # income categories
    ("allowance", "Allowance"),
    ("work", "Work"),
    ("investment returns", "Investment Returns")
]

# Create your models here.
class Entry(models.Model):
    """This is the default entry model"""
    username = models.CharField(max_length=50, default="User")
    entry_type = models.CharField(max_length=50, choices=ENTRY_TYPE_CHOICES, default="income")
    description = models.CharField(max_length=120)
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES, default="food")
    date = models.DateField()
    amount = models.DecimalField(max_digits=20,decimal_places=2)

    def get_absolute_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

