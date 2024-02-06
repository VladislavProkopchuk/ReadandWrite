def read_recipes(file_name):
  recipes = []

  with open(file_name, 'r') as file:
    lines = file.readlines()
    i = 0

    while i < len(lines):
      name = lines[i].strip()
      ingredients_count = int(lines[i + 1])

      ingredients = []
      for j in range(i + 2, i + 2 + ingredients_count):
        ingredient_data = lines[j].strip().split(' | ')
        ingredient = {
          'name': ingredient_data[0],
          'quantity': float(ingredient_data[1]),
          'unit': ingredient_data[2]
        }
        ingredients.append(ingredient)

      recipe = {
        'name': name,
        'ingredients': ingredients
      }
      recipes.append(recipe)

      i += 2 + ingredients_count

  return recipes

  def print_recipe(recipe):
    print(recipe['name'])
    print('Ингредиенты:')
    for ingredient in recipe['ingredients']:
      print(f"{ingredient['name']}: {ingredient['quantity']} {ingredient['unit']}")

  def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
      for ingredient in cook_book[dish]:
        ingredient_name = ingredient['ingredient_name']
        measure = ingredient['measure']
        quantity = ingredient['quantity'] * person_count
        if ingredient_name in shop_list:
          shop_list[ingredient_name]['quantity'] += quantity
        else:
          shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list