# Class for filtering by food type
class FoodTypeFilter:
    def __init__(self, food_type):
        self.food_type = food_type.lower()

    def filter(self, row):
        # Assuming the food type is in the second column (index 1)
        return self.food_type == "no idea" or self.food_type in row[1].lower()

# Class for filtering by price range
class PriceRangeFilter:
    def __init__(self, price_range):
        self.price_range = price_range.lower()

    def filter(self, row):
        # Assuming the price range is in the third column (index 2)
        return self.price_range == "any price" or self.price_range in row[2].lower()
