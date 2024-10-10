"""
Models for the 'Inventory' app.
"""

from django.db import models


class Article(models.Model):
    """Represents an article in the inventory.

    Attributes:
        name (str): The name of the article.
        quantity_at_home (int): The quantity of the article currently at home.
        quantity_to_buy (int): The quantity of the article that needs to be purchased.
        price (Decimal, optional): The price of the article. It can be null or blank.

    Methods:
        increase_quantity(amount): Increases the quantity of the article at home by a specified amount.
        decrease_quantity(amount): Decreases the quantity of the article at home by a specified amount,
            ensuring it does not go below zero.
        add_to_buy(amount): Increases the quantity of the article to buy by a specified amount.
        remove_from_buy(amount): Decreases the quantity of the article to buy by a specified amount,
            ensuring it does not go below zero.
    """

    name = models.CharField(max_length=255)
    quantity_at_home = models.IntegerField(default=0)
    quantity_to_buy = models.IntegerField(default=0)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    # Methods for 'quantity_at_home'
    def increase_quantity(self, amount):
        """Increases the quantity of the article at home.

        Args:
            amount (int): The amount to increase the quantity by.
        """
        self.quantity_at_home += amount
        self.save()

    def decrease_quantity(self, amount):
        """Decreases the quantity of the article at home.

        Args:
            amount (int): The amount to decrease the quantity by. If the quantity is zero, no change occurs.
        """
        if self.quantity_at_home > 0:
            self.quantity_at_home -= amount
        self.save()

    # Methods for 'quantity_to_buy'
    def add_to_buy(self, amount):
        """Increases the quantity of the article to buy.

        Args:
            amount (int): The amount to increase the quantity to buy by.
        """
        self.quantity_to_buy += amount
        self.save()

    def remove_from_buy(self, amount):
        """Decreases the quantity of the article to buy.

        Args:
            amount (int): The amount to decrease the quantity to buy by.
            If the quantity is zero, no change occurs.
        """
        if self.quantity_to_buy > 0:
            self.quantity_to_buy -= amount
        self.save()
