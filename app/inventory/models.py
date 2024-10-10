"""
Models for the 'Inventory' app.
"""
from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=255)
    quantity_at_home = models.IntegerField(default=0)
    quantity_to_buy = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Methods for 'quantity_at_home'
    def increase_quantity(self, amount):
        self.quantity_at_home += amount
        self.save()

    def decrease_quantity(self, amount):
        if self.quantity_at_home > 0:
            self.quantity_at_home -= amount
        self.save()

    # Methods for 'quantity_to_buy'
    def add_to_buy(self, amount):
        self.quantity_to_buy += amount
        self.save()

    def remove_from_buy(self, amount):
        if self.quantity_to_buy > 0:
            self.quantity_to_buy -= amount
        self.save()
