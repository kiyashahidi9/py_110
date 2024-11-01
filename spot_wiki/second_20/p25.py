'''
input: two dictionaries
    - a recipe
    - current ingredients
output: an integer
    - the max number of cakes

rules
    - if an ingredient is missing, no cakes can be made
    - current ingredients not present in the recipe 
        - don't need to be considered
    - the current ingredient divided by the recipe is how many
        of that ingredient can be used in multiple cakes
    - the minimum ingredient is the determining factor

data structure:
    - dictionary
    - a list to keep track of times an ingredient can be used

ALG:
1. take the recipe and the current_ingredients
1.. initialize an ingredient_count list
2. go through each ingredient and quantity in the recipe
    - if the ingredient is not in current_ingredients,
        - return 0
    - divide the current_ingredient value by the recipe value
        - add to ingredient_count list
3. return the minimum of the ingredient_count list
'''

def cakes(recipe, current_ingredients):
    ingredient_count = []
    for ingredient, quantity in recipe.items():
        if ingredient not in current_ingredients:
            return 0
        count = current_ingredients[ingredient] // quantity
        ingredient_count.append(count)
    return min(ingredient_count)

print(cakes({'flour': 500, 'sugar': 200, 'oil': 300}, {'flour': 1200, 'sugar': 300, 'cream': 6000}))