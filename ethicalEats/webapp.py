from flask import Flask, render_template
from flask import request

from db_connector.db_connector import connect_to_database, execute_query

# Creates Flask instance
webapp = Flask(__name__)


@webapp.route('/')
def index():
    return render_template('index.html')


@webapp.route('/recipebook')
def recipebook():
    db_connection = connect_to_database()
    query = "SELECT * from Recipes"
    result = execute_query(db_connection, query).fetchall()
    return render_template('recipebook.html', recipes=result)

@webapp.route('/ingredients/<int:recipe_id>')
def ingredients(recipe_id):
    db_connection = connect_to_database()
    ingredients_query = "select * from Ingredients where ingredientID in (select ingredientID from Recipes_Ingredients where recipeID = %i)" % recipe_id
    ingredients_result = execute_query(db_connection, ingredients_query).fetchall()

    recipe_query = "select * from Recipes where recipeID = %i" % recipe_id
    recipe_result = execute_query(db_connection, recipe_query).fetchall()

    return render_template('ingredients.html', ingredients = ingredients_result, recipe = recipe_result)

@webapp.errorhandler(404)
def heh_error(e):
    return render_template('404.html'), 404


@webapp.errorhandler(500)
def another_heh_error(e):
    return render_template('500.html'), 500


# To start flask locally
# if __name__ == '__main__':
#     webapp.run(debug=True)
