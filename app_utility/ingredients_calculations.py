from app_utility.classes.units_class import Unit
from app_utility.classes.ingredients_classes import Water, Flour, Salt
from app_utility.classes.stage_classes import Ferment, Dough
from app_utility.constants import WATER, SALT, FLOUR_FOR_DOUGH, FLOUR_FOR_FERMENT


def calculate_coefficient(mass_input: int or float) -> int or float:
    coefficient = mass_input / 180

    return coefficient


def count_water(mass_input: int or float) -> int or float:
    return WATER * calculate_coefficient(mass_input)


def count_ferment(mass_input: int or float) -> Ferment:
    water_amount = count_water(mass_input)
    flour_amount = FLOUR_FOR_FERMENT * calculate_coefficient(mass_input)

    return Ferment(Water(water_amount, Unit.MILLILITER),
                   Flour(flour_amount, Unit.GRAM))


def count_dough(mass_input: int or float) -> Dough:
    water_amount = count_water(mass_input)
    flour_amount = FLOUR_FOR_DOUGH * calculate_coefficient(mass_input)
    salt_amount = SALT * calculate_coefficient(mass_input)

    return Dough(Water(water_amount, Unit.MILLILITER),
                 Flour(flour_amount, Unit.GRAM),
                 Salt(salt_amount, Unit.DESSERT_SPOON))
