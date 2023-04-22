from flask import Flask, render_template, request, redirect, url_for
import csv
from drinks_to_ingredients import getDrinks, getIngredients, createName
from ingredient_similarity import create_ingredients

app = Flask("Cockathon")
adjectives = [] # whatever u get from the local storage think mehek
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
    # adjectives = ["fruity", "bubbly"]
    print(f"adjectives are {adjectives}")
    data = request.get_json()
    dataL[0] = ", ".join(data)
    print("Data:", data)
    drinksL[0] = createName(getDrinks(adjectives))
    ingredientsList = create_ingredients(createName, getIngredients(getDrinks(adjectives)), adjectives)
    # drink = getDrinks(data)[0]
    # drinksL[0] = drink
    # ingredientsList = getIngredients(drink)
    ingredients = ", ".join(ingredientsList)
    descriptionsL[0] = ingredients
    # data = request.get_json()
    # dataL[0] = ", ".join(data)
    # print("Data:", data)
    # drinksL[0] = createName(getDrinks(adjectives))
    # ingredientsList = create_ingredients(createName, getIngredients(getDrinks(adjectives)), adjectives)
    print("data:", dataL[0])
    print("drinks:", drinksL[0])
    
    return render_template("drink.html", drinks = drinksL[0], description = descriptionsL[0], data=dataL[0], cache_timeout=0)

@app.route('/new_drinks', methods=['GET'])
def new_drinks():
  return render_template("website.html", drinks = drinksL[0], description = descriptionsL[0], data=dataL[0], cache_timeout=0)

@app.route('/send_array', methods=['POST'])
def send_array():
    ids = request.json['data']
    # Process the array data here
    print(ids)
    adjectives = ids
    # return {'status': 'success'}
    return adjectives


@app.route('/retrieve_drinks', methods=['POST'])
def retrieve_drinks():
    
    print(f"drinksL[0] is {drinksL[0]}")
    print("test")
    # print()
    return render_template("drink.html", cache_timeout=0) # redirect(url_for('show_drinks'))


@app.route('/')
def index():
    return render_template("website.html")


if __name__ == '__main__':
    app.run()

