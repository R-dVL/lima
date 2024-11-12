"""
Models for the 'Inventory' app.
"""

from django.db import models


class Article(models.Model):
    """Represents an article in the inventory.

    Attributes:
        name (str): The name of the article.
        quantity (int): The quantity of the article currently at home.
        price (Decimal, optional): The price of the article. It can be null or blank.

    Methods:
        increase_quantity(amount): Increases the quantity of the article at home.
        decrease_quantity(amount): Decreases the quantity of the article at home,
            ensuring it does not go below zero.
        add_to_buy(amount): Increases the quantity of the article to buy by a specified amount.
        remove_from_buy(amount): Decreases the quantity of the article to buy by a specified amount,
            ensuring it does not go below zero.
    """

    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    # Methods for 'quantity'
    def increase_quantity(self, amount):
        """Increases the quantity of the article at home.

        Args:
            amount (int): The amount to increase the quantity by.
        """
        self.quantity += amount
        self.save()

    def decrease_quantity(self, amount):
        """Decreases the quantity of the article at home.

        Args:
            amount (int): The amount to decrease the quantity by.
        """
        if self.quantity > 0:
            self.quantity -= amount
        self.save()
