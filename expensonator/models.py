from django.db import models
from taggit.managers import TaggableManager

class Expense(models.Model):
    name = models.CharField(max_length=200)
    merchant = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField()

    tags = TaggableManager()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
