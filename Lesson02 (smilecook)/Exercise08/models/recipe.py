recipe_list = []

def get_last_id():

    if recipe_list:
        last_recipe = recipe_list[-1]  # [-1] means the last element in a sequence
    else:
        return 1
    return last_recipe.id + 1

# объявляем класс Recipe
class Recipe:

    # !!! В одном классе всегда только один конструктор
    # Определяем метод (конструктор) init, который примет параметры name, description ...etc
    def __init__(self, name, description, num_of_servings, cook_time, directions):
        self.id = get_last_id()
        self.name = name
        self.description = description
        self.num_of_servings = num_of_servings
        self.cook_time = cook_time
        self.directions = directions
        self.is_publish = False

    # Use @property decorator on any method in the class to use the method as a property.
    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'num_of_servings': self.num_of_servings,
            'cook_time': self.cook_time,
            'directions': self.directions
        }