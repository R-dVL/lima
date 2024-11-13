"""
Models for the 'Inventory' app.
"""

from django.db import models



class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    quantity_to_buy = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def increase_quantity(self, amount):
        self.quantity += amount
        self.save()

    def decrease_quantity(self, amount):
        if self.quantity > 0:
            self.quantity -= amount
        self.save()

    def total_cost(self):
        """Calculates the total cost for the remaining quantity needed to reach `quantity_to_buy`."""
        quantity_needed = max(self.quantity_to_buy - self.quantity, 0)
        return quantity_needed * self.price