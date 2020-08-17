def calculate_coefficient(mass_input: int or float) -> int or float:
    coefficient = mass_input / 180

    return coefficient


def count_ingredients_mass_first(mass_input: int or float) -> dict:
    water = 150 * calculate_coefficient(mass_input)
    flour = 50 * calculate_coefficient(mass_input)

    ingredients = {"Вода: ": str(water) + " миллилитров",
                   "Мука: ": str(flour) + " граммов"}

    return ingredients


def count_ingredients_mass_second(mass_input: int or float) -> dict:
    water = 150 * calculate_coefficient(mass_input)
    flour = 320 * calculate_coefficient(mass_input)
    salt = calculate_coefficient(mass_input)

    ingredients = {"Вода: ": str(water) + " миллилитров",
                   "Мука: ": str(flour) + " граммов",
                   "Соль: ": str(salt) + " дессертных ложек"}

    return ingredients
