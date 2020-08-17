from app_utility.classes.ingredients_classes import Water, Flour, Salt


class Ferment:
    def __init__(self, water: Water, flour: Flour):
        self.water = water
        self.flour = flour


class Dough:
    def __init__(self, water: Water, flour: Flour, salt: Salt):
        self.water = water
        self.flour = flour
        self.salt = salt
