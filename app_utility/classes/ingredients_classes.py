from app_utility.ingredients_calculations import Unit


class Water:
    def __init__(self, amount: int or float, unit: Unit) -> None:
        self.amount = amount
        self.unit = unit


class Flour:
    def __init__(self, amount: int or float, unit: Unit) -> None:
        self.amount = amount
        self.unit = unit


class Salt:
    def __init__(self, amount: int or float, unit: Unit) -> None:
        self.amount = amount
        self.unit = unit
