from django.db import models
from taggit.managers import TaggableManager

class Expense(models.Model):
    name = models.CharField(max_length=200)
    merchant = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    date = model.DateField()

    tags = TaggableManager()

    created = mdoels.DateTimeField(auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=False)
