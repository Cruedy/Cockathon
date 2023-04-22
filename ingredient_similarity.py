# https://towardsdatascience.com/semantic-similarity-using-transformers-8f3cb5bf66d6
# follow this, but basically run
# pip install transformers
# pip install sentence-transformers

from sentence_transformers import SentenceTransformer, util
import random
# import numpy as np

from drinks_to_ingredients import getDrinks, createName, getIngredients

# inputs: word2vec model, list of final drink, list of ingredients from initial drinks, adjectives
# outputs: list of ingredients to represent final drink
#          1-2 alcohol ingredients, 1-2 adjective ingredients, 1-2 other ingredients, 1-2 ingredients from name
def create_ingredients(name, ingredients, adjectives):
    model = SentenceTransformer('stsb-roberta-large')

    alochol_max_similarity = 0.2
    adjective_max_similarity = 0.2
    name_max_similarity = 0.2
    alcohol_ingredients = []
    adjective_ingredients = []
    name_ingredients = []

    for i in ingredients:
        # encode sentences to get their embeddings
        embedding_i = model.encode(i, convert_to_tensor=True)

        # similarities to "alcohol"
        embedding_alcohol = model.encode("alcohol", convert_to_tensor=True)
        alcohol_cosine_scores = util.pytorch_cos_sim(embedding_i, embedding_alcohol)
        # print(f"Similarity score: {alcohol_cosine_scores.item()} with {i} and alcohol")
        if alcohol_cosine_scores >= alochol_max_similarity and i not in alcohol_ingredients:
            alcohol_ingredients.append(i)
            alochol_max_similarity = alcohol_cosine_scores

        # similarities to adjectives
        for adj in adjectives:
            embedding_adj = model.encode(adj, convert_to_tensor=True)
            adj_cosine_scores = util.pytorch_cos_sim(embedding_i, embedding_adj)
            # print(f"Similarity score: {adj_cosine_scores.item()} with {i} and {adj}")
            if adj_cosine_scores >= adjective_max_similarity and i not in adjective_ingredients and i not in alcohol_ingredients:
                adjective_ingredients.append(i)
                adjective_max_similarity = adj_cosine_scores
        
        # similarities to the name of the drink
        name_words = name.split(" ")
        for name_word in name_words:
            embedding_name = model.encode(name_word, convert_to_tensor=True)
            name_cosine_scores = util.pytorch_cos_sim(embedding_i, embedding_name)
            # print(f"Similarity score: {name_cosine_scores.item()} with {i} and {name_word}")
            if name_cosine_scores >= name_max_similarity and i not in name_ingredients and i not in adjective_ingredients and i not in alcohol_ingredients:
                name_ingredients.append(i)
                name_max_similarity = name_cosine_scores
        
    print(f"alcohol_ingredients are {alcohol_ingredients}")
    print(f"adjective_ingredients are {adjective_ingredients} with adjectives {adjectives}")
    print(f"name_ingredients are {name_ingredients} with name {name}")

    num_alcohol = random.randint(1,2)
    num_adj = random.randint(2, 3)
    num_name = random.randint(1, 2)

    # ensuring that we do not sample a size larger than the length of every ingredient
    if len(alcohol_ingredients) < num_alcohol:
        num_alcohol = len(alcohol_ingredients)
    if len(adjective_ingredients) > 3:
        adjective_ingredients = adjective_ingredients[-3:]
    elif len(adjective_ingredients) < num_adj:
        num_adj = len(adjective_ingredients)
    if len(name_ingredients) > 3:
        name_ingredients = name_ingredients[-3:]
    elif len(name_ingredients) < num_name:
        num_name = len(name_ingredients)

    random_alcohol = random.sample(alcohol_ingredients, k=num_alcohol)
    random_adj = random.sample(adjective_ingredients, k=num_adj)
    random_name = random.sample(name_ingredients, k=num_name)

    return random_alcohol + random_adj + random_name

adjectives = ["mild"]
drinks = getDrinks(adjectives)
name = createName(drinks)
ingredients = getIngredients(drinks)
print(ingredients)
print(name)
print(create_ingredients(name, ingredients, adjectives))