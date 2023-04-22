
# Cockathon

In this Cockathon, we created a website that takes in adjectives that you want your cocktail to be and outputs a name and list of ingredients of your cocktail.

# Ideation
We first completed a round of ideation to brainstorm what we wanted our website to look like and what we wanted to generate for our future cocktail.
![Ideation](https://github.com/Cruedy/Cockathon/blob/main/IMG_6992.JPG)

# Implementation
Here are some aspects we included in this project:
- web scraping -> to obtain a database of drink names and ingredients from https://www.thecocktaildb.com
- semantic similarity (pytorch, transformers) -> to compute the similarity score between two phrases, like "summer" and "1 juice of an orange"
- flask -> to connect our front-end to our back-end

# Reflections
Although we are proud of what we have created so far in the span of a week, here are some further improvements we would like to make
- optimizing the generation of ingredients for our drink
- adding a loading page
- adding instructions for the ingredients
- adding limits on the amount of alcohol added to the generated drink
