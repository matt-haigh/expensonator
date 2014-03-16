from django.db import models
from taggit.managers import TaggableManager

class Expense(models.Model):
    name = models.CharField(max_length=200)
    merchant = models.CharField(max_length=200, blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField()

    BUDGET_CATEGORY_ENTERTAINMENT = u"Entertainment"
    BUDGET_CATEGORY_FOOD = u"Food"
    BUDGET_CATEGORY_GIFTS = u"Gifts"
    BUDGET_CATEGORY_MISC = u"Misc"
    BUDGET_CATEGORY_NONE = u"None"
    BUDGET_CATEGORY_RENT = u"Rent"
    BUDGET_CATEGORY_TRANSPORTATION = u"Transportation"
    BUDGET_CATEGORY_TRAVEL = u"Travel"
    BUDGET_CATEGORY_UTILITIES = u"Utilities"
    BUDGET_CATEGORY_CHOICES = (
        (BUDGET_CATEGORY_ENTERTAINMENT, BUDGET_CATEGORY_ENTERTAINMENT),
        (BUDGET_CATEGORY_FOOD, BUDGET_CATEGORY_FOOD),
        (BUDGET_CATEGORY_GIFTS, BUDGET_CATEGORY_GIFTS),
        (BUDGET_CATEGORY_MISC, BUDGET_CATEGORY_MISC),
        (BUDGET_CATEGORY_NONE, BUDGET_CATEGORY_NONE),
        (BUDGET_CATEGORY_RENT, BUDGET_CATEGORY_RENT),
        (BUDGET_CATEGORY_TRANSPORTATION, BUDGET_CATEGORY_TRANSPORTATION),
        (BUDGET_CATEGORY_TRAVEL, BUDGET_CATEGORY_TRAVEL),
        (BUDGET_CATEGORY_UTILITIES, BUDGET_CATEGORY_UTILITIES))
    BUDGET_CATEGORY_DEFAULT = BUDGET_CATEGORY_NONE
    budget_category = models.CharField(
        max_length=20,
        choices=BUDGET_CATEGORY_CHOICES,
        default=BUDGET_CATEGORY_DEFAULT)

    tags = TaggableManager()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)

    def tags_as_string(self):
        return " ".join(self.tags.names())

    def reset_tags_from_string(self, tags_string):
        self.tags.clear()
        for tag in tags_string.split(" "):
            self.tags.add(tag)
