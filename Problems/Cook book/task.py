pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()
recipe_dict = {"pasta": pasta, "apple pie": apple_pie,
               "ratatouille": ratatouille, "chocolate cake": chocolate_cake,
               "omelette": omelette}

for key, value in recipe_dict.items():
    if ingredient in value:
        print("{0} time!".format(key))
