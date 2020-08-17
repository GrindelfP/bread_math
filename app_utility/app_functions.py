from flask import Flask, render_template, request
from app_utility.ingredients_calculations import count_ferment, count_dough, Unit

app = Flask(__name__)


# noinspection PyUnresolvedReferences
@app.route("/")
def greetings() -> "html":
    return render_template("greetings_and_input.html")


# noinspection PyUnresolvedReferences
@app.route("/calculate",  methods=["POST"])
def show_results() -> "html":
    mass = request.form["mass_input"]
    if mass.count(".") > 0:
        mass = float(mass)
    else:
        mass = int(mass)
    ingredients_ferment = count_ferment(mass)
    ingredients_dough = count_dough(mass)
    return render_template("output.html",
                           # ingredients_list_length=len(ingredients_ferment),
                           ingredients_ferment=ingredients_ferment,
                           ingredients_dough=ingredients_dough)


@app.context_processor
def localization() -> dict:
    def localize_units(unit: Unit) -> str:
        if unit == Unit.MILLILITER:
            return "миллилитров"
        elif unit is Unit.GRAM:
            return "граммов"
        elif unit is Unit.DESSERT_SPOON:
            return "дессертных ложек"
    return dict(localize_units=localize_units)