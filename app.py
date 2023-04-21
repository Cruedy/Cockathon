from flask import Flask, render_template, request, redirect, url_for
import csv
import drinks_to_ingredients

app = Flask("Cockathon")
dataL = [0]
drinksL = [0]
descriptionsL = [0]

# def getDrinks(tags):
#   drinks = []
#   for t in tags:
#     per_tag = []
#     with open("Tags.csv", "r") as file:
#       csvreader = csv.reader(file)
#       for row in csvreader:
#         #print(row)
#         if t in row[1]:
#           per_tag.append(row[0])
#     file.close()
#     drinks.append(per_tag)
#   return drinks

@app.route('/show_drinks', methods=['GET'])
def show_drinks():
  print("data:", dataL[0])
  print("drinks:", drinksL[0])
  return render_template("loader.html", drinks = drinksL[0], description = descriptionsL[0], data=dataL[0], cache_timeout=0)

@app.route('/retrieve_drinks', methods=['POST'])
def retrieve_drinks():
    data = request.get_json()
    dataL[0] = ", ".join(data)
    # print("Data:", data)
    drink = drinks_to_ingredients.getDrinks(data)[0]
    drinksL[0] = drink
    ingredientsList = drinks_to_ingredients.getIngredients(drink)
    ingredients = ", ".join(ingredientsList)
    descriptionsL[0] = ingredients
    # print(drinks)
    # print("test")
    # print()
    return render_template("drink.html", cache_timeout=0) # redirect(url_for('show_drinks'))


@app.route('/')
def index():
    return render_template("website.html")


if __name__ == '__main__':
    app.run()

