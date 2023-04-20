import csv
import random

# takes in adjectives, like sweet, fruity
# outputs a list of drinks that are already in our ingredients.csv
def getDrinks(tags):
  drinks = []
  for t in tags:
    with open("Tags.csv", "r") as file:
      csvreader = csv.reader(file)
      for row in csvreader:
        if t in row[1]:
          drinks.append(row[0])
  return drinks

# inputs a list of drinks that are in our ingredients.csv
# outputs the list of ingredients in those drinks
def getIngredients(drinks):
    ingredients = []
    with open("Ingredients.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if row[0] in drinks:
                #row[1] is a string
                no_outside_quotes = row[1][1:-1].split(",")
                # print(no_outside_quotes)
                ingredients.append(no_outside_quotes[0][1:-1])
                for ingredient in no_outside_quotes[1:]:
                    # print(ingredient)
                    ingredient_no_quotes = ingredient[2:-1]
                    ingredients.append(ingredient_no_quotes)
    return ingredients

# helper for createName
def handle_loop(adj, alc, max, name, drinks):
    for d in drinks:
        terms = d.split()
        if len(terms) > max:
            max = len(terms)
        alc.append(terms.pop(len(terms)-1))
        for t in terms:
            adj.append(t)
    for i in range(max - 1):
        num = random.randint(0, len(adj)-1)
        name = name + adj[num] + " "
        adj.pop(num)
    num = random.randint(0, len(alc)-1)
    name = name + alc[num] + " "
    return name

# inputs a list of drink names
# outputs a super cool name of a drink
def createName(drinks):
    adj = []
    alc = []
    print(drinks)
    name = handle_loop(adj, alc, 0, "", drinks)
    while name in drinks[0]:
        name = handle_loop(adj, alc, 0, "", drinks)
    return name
