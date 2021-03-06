from flask import Flask, jsonify, request
from http import HTTPStatus

 # If you are using a single module, __name__ is the correct value.
# If you are using a package, it’s recommended to hardcode the name of your package.
# For more information look at: https://flask-russian-docs.readthedocs.io/ru/latest/api.html#flask.Flask
app = Flask(__name__)  # If you are using a single module, __name__ is the correct value.
# If you are using a package, it’s recommended to hardcode the name of your package.
# For more information look at: https://flask-russian-docs.readthedocs.io/ru/latest/api.html#flask.Flask

recipes = [

    {

        'id': 1,
        'name': 'Egg Salad',
        'description': 'This is a lovely egg salad recipe.'

    },

    {

        'id': 2,
        'name': 'Tomato Pasta',
        'description': 'This is a lovely tomato pasta recipe.'

    }

]
# Переменная recipes содержит список??? [], внутри, которого словарь {}


@app.route("/")  # http://127.0.0.1:5000/
def hello():
    return "Hello World!"


@app.route('/recipes', methods=['GET'])
def get_recipes():
    # возвращает в формате JSON репрезентацию аргументов функции
    # jsonify function to convert the list of recipes to JSON format and respond to the client:
    # можно записать просто как return jsonify(recipes) ???
    return jsonify({'data': recipes})


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    # The next(iterator, default) function returns the next item from the iterator.
    # default (optional) - this value is returned if the iterator is exhausted (there is no next item)
    # recipe for recipe in recipes if recipe['id'] == recipe_id
    # Это генератор, который позволяет в одну строку создать список, наполненный значениями
    # the line for recipe in recipes iterates through all the recipes in our recipe collection
    # and finds out the recipe with id = recipe_id. Once we have found it, we store it in the iterator
    # and retrieve it using the next function.
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)


    if recipe:
        return jsonify(recipe)

    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND


@app.route('/recipes', methods=['POST'])
def create_recipe():
    # request.get_json method to get the name and description from the client POST request.
    # Flask предоставляет метод request.get_json(), чтобы извлечь JSON из запроса и вернуть его в виде структуры Python.
    # Этот метод возвращает None, если данные JSON не найдены в запросе, поэтому я могу гарантировать, что я всегда
    # получаю словарь, используя запрос request.get_json()
    data = request.get_json()


    name = data.get('name')
    description = data.get('description')

    recipe = {
        'id': len(recipes) + 1,
        'name': name,
        'description': description
    }

    recipes.append(recipe)

    return jsonify(recipe), HTTPStatus.CREATED


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

    data = request.get_json()

    recipe.update(
        {
            'name': data.get('name'),
            'description': data.get('description')
        }
    )

    return jsonify(recipe)


@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

    recipes.remove(recipe)

    return jsonify({'message': 'recipe deleted'}), HTTPStatus.NO_CONTENT



if __name__ == '__main__':
    app.run()