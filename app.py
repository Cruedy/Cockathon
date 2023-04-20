from flask import Flask, render_template, request
import csv

app = Flask("Cockathon")

def getDrinks(tags):
  drinks = []
  for t in tags:
    per_tag = []
    with open("Tags.csv", "r") as file:
      csvreader = csv.reader(file)
      for row in csvreader:
        #print(row)
        if t in row[1]:
          per_tag.append(row[0])
    drinks.append(per_tag)
  return drinks

@app.route('/retrieve_drinks', methods=['POST'])
def retrieve_drinks():
    data = request.get_json()
    print("Data:", data)
    drinks = getDrinks(data)
    print(drinks)
    print()
    return render_template("website.html")


@app.route('/')
def index():
    return render_template("website.html")


if __name__ == '__main__':
    app.run()

