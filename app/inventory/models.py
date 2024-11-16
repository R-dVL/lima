"""
Models for the 'Inventory' app.
"""
from django.db import models

class List(models.Model):
    """Represents a list of items in the inventory."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='list_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    """Represents an item in the inventory.

    Attributes:
        name (str): The name of the item.
        description (str, optional): A brief description of the item.
        amount (int): The current stock amount of the item.
        amount_to_buy (int): The desired stock amount of the item.
        price (Decimal, optional): The price of the item. Can be null or blank.
        list (ForeignKey): The associated list for the item.

    Methods:
        increase_amount(amount): Increases the amount in stock.
        decrease_amount(amount): Decreases the amount in stock without going below zero.
        total_cost(): Calculates the total cost to reach the desired stock amount.
    """
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(default=0)
    amount_to_buy = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')

    def increase_amount(self, amount):
        """Increases the amount in stock by the given amount."""
        self.amount += amount
        self.save()

    def decrease_amount(self, amount):
        """Decreases the amount in stock by the given amount, ensuring it does not go below zero."""
        if self.amount > 0:
            self.amount -= amount
        self.save()

    def total_cost(self):
        """Calculates the total cost to buy the remaining amount needed to reach `amount_to_buy`."""
        amount_needed = max(self.amount_to_buy - self.amount, 0)
        return amount_needed * self.price

    def __str__(self):
        return self.name
