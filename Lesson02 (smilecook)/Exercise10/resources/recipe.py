from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.recipe import Recipe, recipe_list


#
# RecipeListResource class has GET and POST methods, which are used to get and create the recipe's resources
# RecipeListResource class inherits from flask-restful.Resource.
class RecipeListResource(Resource):

    # get method is for, getting all the public recipes back.
    # It does this by declaring a data list and getting all the recipes with is_publish = true in recipe_list.
    # These recipes are appended to our data list and returned to the users.
    def get(self):

        data = []

        for recipe in recipe_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {'data': data}, HTTPStatus.OK

    # post method is used to create the recipe
    def post(self):
        data = request.get_json()

        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        num_of_servings=data['num_of_servings'],
                        cook_time=data['cook_time'],
                        directions=data['directions'])

        recipe_list.append(recipe)

        return recipe.data, HTTPStatus.CREATED


# RecipeResource also inherits from flask-restful.Resource.
class RecipeResource(Resource):

    # The get method we are implementing here is getting back a single recipe.
    # We do that by searching for recipe_id in recipe_list.
    # We will only get back those recipes with is_publish = true.
    # If no such recipe is found, we will return the message recipe not found.
    def get(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id and recipe.is_publish == True), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        return recipe.data, HTTPStatus.OK

    # The put method gets the recipe details from the client request using request.get_json, updates the recipe object.
    # Then, it returns the HTTP status code 200 OK if everything goes well.
    def put(self, recipe_id):
        data = request.get_json()

        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.name = data['name']
        recipe.description = data['description']
        recipe.num_of_servings = data['num_of_servings']
        recipe.cook_time = data['cook_time']
        recipe.directions = data['directions']

        return recipe.data, HTTPStatus.OK


# the recipes can have two Statuses (unpublished and published).
# This allows the user to continue updating their unpublished recipes before publishing them to the world

# RecipePublishResource inherits from flask_restful.Resource
class RecipePublishResource(Resource):

    # The put method will locate the recipe with the passed-in recipe_id and update the is_publish status to true.
    # Then, it will return HTTPStatus.NO_CONTENT, which shows us that the recipe has been published successfully.
    def put(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    # The delete method is the opposite of the put method.
    # Instead of setting is_publish to true, it sets it to false in order to unpublish the recipe.
    def delete(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = False

        return {}, HTTPStatus.NO_CONTENT