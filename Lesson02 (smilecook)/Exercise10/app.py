from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource

# If you are using a single module, __name__ is always the correct value.
# If you however are using a package, it’s usually recommended to hardcode the name of your package there.
# For more information: https://flask-russian-docs.readthedocs.io/ru/0.10.1/api.html#flask.Flask
app = Flask(__name__)
api = Api(app)

api.add_resource(RecipeListResource, '/recipes')
# <int: recipe_id > is a placeholder for the recipe ID.
# When a GET HTTP request has been sent to the route "/recipes/2" URL,
# this will invoke the get method under RecipeResource with a parameter, that is, recipe_id = 2.
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')

if __name__ == '__main__':
    app.run(port=5000, debug=True)