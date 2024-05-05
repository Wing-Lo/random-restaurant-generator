# Class for filtering by food type
class FoodTypeFilter:
    def __init__(self, choice):
        self.choice = choice

    def filter(self, restaurant):
        return restaurant[1].lower() == self.choice.lower()

# Class for filtering by price range
class PriceRangeFilter:
    def __init__(self, choice):
        self.choice = choice

    def filter(self, restaurant):
        return restaurant[2].lower() == self.choice.lower() 