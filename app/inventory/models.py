"""
Models for the 'inventory' app.
"""
from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity_at_home = models.PositiveIntegerField(default=0)
    quantity_to_buy = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def increase_quantity(self, amount):
        self.quantity_at_home += amount
        self.save()

    def decrease_quantity(self, amount):
        if self.quantity_at_home >= amount:
            self.quantity_at_home -= amount
            self.save()
        else:
            raise ValueError("Cannot reduce the quantity below zero.")

    def add_to_buy(self, amount):
        self.quantity_to_buy += amount
        self.save()

    def remove_from_buy(self, amount):
        if self.quantity_to_buy >= amount:
            self.quantity_to_buy -= amount
            self.save()
        else:
            raise ValueError("Cannot reduce the quantity to buy below zero.")

    def __str__(self):
        return self.name
