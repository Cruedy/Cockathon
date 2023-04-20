import csv
import itertools

# takes in adjectives, like sweet, fruity, and outputs a list of drinks that are already in our ingredients.csv
def getDrinks(tags):
    drinks = []
    for t in tags:
        per_tag = []
        with open("Tags.csv", "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                # print(row)
                if t in row[1]:
                    per_tag.append(row[0])
        drinks.append(per_tag)
    return drinks


# inputs a list of drinks that are in our ingredients.csv
# outputs the list of ingredients in those drinks
def getIngredients(drinks):
    ingredients = []
    with open("Ingredients.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] in drinks[0]:
                #row[1] is a string
                no_outside_quotes = row[1][1:-1].split(",")
                # print(no_outside_quotes)
                ingredients.append(no_outside_quotes[0][1:-1])
                for ingredient in no_outside_quotes[1:]:
                    # print(ingredient)
                    ingredient_no_quotes = ingredient[2:-1]
                    ingredients.append(ingredient_no_quotes)
    return ingredients

# getIngredients(getDrinks(["fruity"]))
print(getIngredients(getDrinks(["fruity"])))

# print(getDrinks(["fruity"]))
# print('Banana Daiquiri' + " " in getDrinks(["fruity"])[0])
