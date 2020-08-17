from flask import Flask, render_template, request
from ingredients_calculations import count_ingredients_mass_first, count_ingredients_mass_second

app = Flask(__name__)


@app.route("/")
def greetings() -> "html":
    return render_template("greetings_and_input.html")


@app.route("/calculate",  methods=["POST"])
def show_results() -> "html":
    mass = request.form["mass_input"]
    if mass.count(".") > 0:
        mass = float(mass)
    else:
        mass = int(mass)
    ingredients_dict_first = count_ingredients_mass_first(mass)
    ingredients_dict_second = count_ingredients_mass_second(mass)
    return render_template("output.html",
                           ingredients_list_length=len(ingredients_dict_first),
                           ingredients_dict_first=ingredients_dict_first,
                           ingredients_dict_second=ingredients_dict_second)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
