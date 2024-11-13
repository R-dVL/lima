"""
Custom filters for 'inventory' app
"""
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """
    Multiply the value by the argument.

    Args:
        value (numeric): The value to be multiplied.
        arg (numeric): The number to multiply with the value.

    Returns:
        numeric: The result of multiplying the value and the argument, or 0 if an error occurs.
    """
    try:
        return value * arg
    except (TypeError, ValueError):
        # If there is an error (e.g., invalid types for multiplication), return 0
        return 0
