"""
This module contains classes for filtering restaurant data by specific criteria.
It includes `FoodTypeFilter` for filtering by food type, and `PriceRangeFilter`
for filtering by price range. These classes are intended to be used when parsing
through a dataset of restaurant information, allowing for a narrowed down selection
based on user preferences or search criteria.

Classes:
    FoodTypeFilter:
        Filters restaurant data based on a specified food type. It checks if the
        provided food type matches the food type listed in a row of restaurant data.

    PriceRangeFilter:
        Filters restaurant data based on a specified price range. It checks if the
        provided price range matches the price range listed in a row of restaurant data.

Usage:
    These filter classes can be instantiated with a specific criterion (food type or 
    price range) and then used to call the `filter` method on rows of restaurant data.
    The `filter` method returns a boolean indicating whether the row meets the filter
    criteria.

Example:
    >>> food_filter = FoodTypeFilter("italian")
    >>> food_filter.filter(["Luigi's Pizzeria", "Italian", "Mid-range"])
    True

    >>> price_filter = PriceRangeFilter("$$")
    >>> price_filter.filter(["Luigi's Pizzeria", "Italian", "Mid-range"])
    True
"""
class FoodTypeFilter:
    """Class for filtering restaurants by food type."""

    def __init__(self, food_type):
        """
        Initialize the filter with a specific food type.
        
        Args:
            food_type (str): The food type to filter by.
        """
        self.food_type = food_type.lower()

    def filter(self, row):
        """
        Filter a row of restaurant data by the food type.
        
        Args:
            row (list): A list representing a row of restaurant data.
        
        Returns:
            bool: True if the row matches the food type, False otherwise.
        """
        # Assuming the food type is in the second column (index 1)
        return self.food_type == "no idea" or self.food_type in row[1].lower()


class PriceRangeFilter:
    """Class for filtering restaurants by price range."""

    def __init__(self, price_range):
        """
        Initialize the filter with a specific price range.
        
        Args:
            price_range (str): The price range to filter by.
        """
        self.price_range = price_range.lower()

    def filter(self, row):
        """
        Filter a row of restaurant data by the price range.
        
        Args:
            row (list): A list representing a row of restaurant data.
        
        Returns:
            bool: True if the row matches the price range, False otherwise.
        """
        # Assuming the price range is in the third column (index 2)
        return self.price_range == "any price" or self.price_range in row[2].lower()
