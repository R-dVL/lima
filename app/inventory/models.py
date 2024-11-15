"""
Models for the 'Inventory' app.
"""
from django.db import models



class Article(models.Model):
    """Represents an article in the inventory.

    Attributes:
        name (str): The name of the article.
        description (str): Brief description of the article.
        quantity (int): The quantity of the article currently in stock.
        quantity_to_buy (int): The quantity of the article desired in stock.
        price (Decimal, optional): The price of the article. It can be null or blank.

    Methods:
        increase_quantity(amount): Increases the quantity of the article in stick.
        decrease_quantity(amount): Decreases the quantity of the article in stock,
            ensuring it does not go below zero.
        total_cost(self): Calculates the price of the amount to buy to reach the
            desired stock quantity.
    """
    name = models.CharField(max_length=255)
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    quantity = models.IntegerField(default=0)
    quantity_to_buy = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def increase_quantity(self, amount):
        """
        Increases the amount in stock.
        """
        self.quantity += amount
        self.save()

    def decrease_quantity(self, amount):
        """
        Decreases the amount in stock.
        """
        if self.quantity > 0:
            self.quantity -= amount
        self.save()

    def total_cost(self):
        """
        Calculates the total cost for the remaining quantity needed to reach `quantity_to_buy`.
        """
        quantity_needed = max(self.quantity_to_buy - self.quantity, 0)
        return quantity_needed * self.price
