def GetLines():
    with open("day21\\entries.txt") as f:
        entries = f.read()
    return entries.split('\n')

def ParseEntries(entries):
    foodsList = list()
    allergenesDict = {}
    ingredientsDict = {}
    for entry in entries:
        infos = entry.split(' (contains ')
        ingredients = infos[0].split(' ')
        for ingredient in ingredients:
            if ingredient not in ingredientsDict:
                ingredientsDict[ingredient] = None
        allergene = infos[1][:-1]
        allergenes = allergene.split(', ')  
        for allergene in allergenes:
            if allergene not in allergenesDict:
                allergenesDict[allergene] = None    
        food = {
            'ingredients': ingredients,
            'allergenes': allergenes
        } 
        foodsList.append(food)
    return foodsList, allergenesDict, ingredientsDict

def AssignIngredientsToAllergenes(allergenes, foods, ingredients):
    for allergene in allergenes:
        possibleIngredients = list(ingredients.keys())
        for food in foods:
            if allergene in food['allergenes']:
                possibleIngredients = FilerElements(possibleIngredients, food['ingredients'])
        allergenes[allergene] = possibleIngredients
    return allergenes

def AssignAllergenesToIngredients(ingredients, allergenes):
    changed = True
    while changed:
        changed = False
        for allergene in allergenes:
            if len(allergenes[allergene]) == 1:
                ingredient = allergenes[allergene][0]
                ingredients[ingredient] = allergene
                allergenes = CleanDict(allergenes, ingredient)
                changed = True
    return ingredients

def CleanDict(dictionary, value):
    for key in dictionary:
        if value in dictionary[key]:
            dictionary[key].remove(value)
    return dictionary 

def FilerElements(list_to_filter, filter_list):
    filtered_list = list()
    for e in list_to_filter:
        if e in filter_list:
            filtered_list.append(e)
    return filtered_list

def CreateCanonicalIngredientsString(ingredients):
    danger_ingredients = {}
    for ingredient in ingredients:
        if ingredients[ingredient] is not None:
            danger_ingredients[ingredient] = ingredients[ingredient]
    sorted_dict = dict(sorted(danger_ingredients.items(), key=lambda item: item[1]))
    sorted_list = list(sorted_dict.keys())
    return ','.join(sorted_list)

if __name__ == "__main__":
    entries = GetLines()
    foods, allergenes, ingredients = ParseEntries(entries)
    allergenes = AssignIngredientsToAllergenes(allergenes, foods, ingredients)
    ingredients = AssignAllergenesToIngredients(ingredients, allergenes)
    dangerousIngredientsString = CreateCanonicalIngredientsString(ingredients)
    print(dangerousIngredientsString)