from flask import Flask, render_template, request, url_for, session, redirect, flash
from ethicalEats.db_connector import connect_to_database, execute_query
#from flask_mysqldb import MySQL
#import MySQLdb.cursors
import re

# Creates Flask instance
webapp = Flask(__name__)
webapp.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@webapp.route('/')
@webapp.route('/landing')
def landing():
    return render_template('landing.html')

@webapp.route('/index')
def index():
    db_connection = connect_to_database()
    query = "SELECT * from Recipes"
    result = execute_query(db_connection, query).fetchall()
    return render_template('index.html', recipes=result)

@webapp.route('/about')
def about():
	return render_template("about.html")

@webapp.route('/recipebook/<int:user_id>')
def recipebook(user_id):
    db_connection = connect_to_database()
    query = "SELECT * from Recipes where recipeID in (select recipeID from Recipes_Users where userID = %i)" % user_id
    result = execute_query(db_connection, query).fetchall()
    return render_template('recipebook.html', recipes=result, userid=user_id)

@webapp.route('/ingredients/<int:recipe_id>')
def ingredients(recipe_id):
    db_connection = connect_to_database()
    ingredients_query = "select * from Ingredients where ingredientID in (select ingredientID from Recipes_Ingredients where recipeID = %i)" % recipe_id
    ingredients_result = execute_query(db_connection, ingredients_query).fetchall()

    recipe_query = "select * from Recipes where recipeID = %i" % recipe_id
    recipe_result = execute_query(db_connection, recipe_query).fetchall()

    alternative_query = "SELECT ei.ethicalIngredientID, ei.ingredientName, ei.description FROM EthicalIngredients as ei INNER JOIN Ingredients_EthicalIngredients as iei ON ei.ethicalIngredientID = ei.ethicalIngredientID INNER JOIN Ingredients as i ON iei.ingredientID = i.ingredientID"
    alternative_result = execute_query(db_connection, recipe_query).fetchall()

    #return render_template('ingredients.html', ingredients = ingredients_result, recipe = recipe_result)
    return render_template('ingredients.html', ingredients = ingredients_result, recipe = recipe_result, alternative = alternative_result)

@webapp.route('/ingredients_user/<int:recipe_id>')
def ingredients_user(recipe_id):
    db_connection = connect_to_database()
    ingredients_query = "select * from Ingredients where ingredientID in (select ingredientID from Recipes_Ingredients where recipeID = %i)" % recipe_id
    ingredients_result = execute_query(db_connection, ingredients_query).fetchall()

    recipe_query = "select * from Recipes where recipeID = %i" % recipe_id
    recipe_result = execute_query(db_connection, recipe_query).fetchall()

    alternative_query = "SELECT ei.ethicalIngredientID, ei.ingredientName, ei.description FROM EthicalIngredients as ei INNER JOIN Ingredients_EthicalIngredients as iei ON ei.ethicalIngredientID = ei.ethicalIngredientID INNER JOIN Ingredients as i ON iei.ingredientID = i.ingredientID"
    alternative_result = execute_query(db_connection, recipe_query).fetchall()

    #return render_template('ingredients.html', ingredients = ingredients_result, recipe = recipe_result)
    return render_template('ingredients.html', ingredients = ingredients_result, recipe = recipe_result, alternative = alternative_result)

@webapp.route('/login')
def login():
    return render_template("login.html")

@webapp.route('/user_login', methods=['POST', 'GET'])
def user_login():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('landing.html')
    elif request.method == 'POST':
        userName = request.form['username']
        userPassword = request.form['password']

        userquery = 'SELECT * FROM Users where userName = %s and userPassword = %s'

        # login info matches an existing account
        if userquery:
            data = (userName, userPassword)
            result = execute_query(db_connection, userquery, data).fetchall()

            recipequery = 'SELECT * FROM Recipes'
            recipesresult = execute_query(db_connection, recipequery).fetchall()

        # Note: keeps saying UndefinedError: tuple object has no element 0
        # login info does not match any existing accounts
        else:
            flash('Incorrect login/password. Account not found.')
            return redirect(request.url)   # shows flash message and stays on current page
        
        return render_template('index_user.html', user=result, recipes=recipesresult)

@webapp.route('/createAccount')
def createAccount():
    return render_template("createAccount.html")

@webapp.route('/new_user_login', methods = ['GET', 'POST'])
def new_user_login():
    db_connection = connect_to_database()

    if request.method == 'GET':
        return render_template('landing.html')

    elif request.method == 'POST':
        userName = request.form['username']
        userPassword = request.form['password']
        userEmail = request.form['email']
        
        # existAcctQuery = 'SELECT * FROM Users WHERE userName = %s'

        # # login info matches an existing account
        # if existAcctQuery:
        #     data = (userName)
        #     failed = execute_query(db_connection, existAcctQuery, data).fetchall()
        #     flash('This username already exists. Please try another.')
        #     # return redirect('createAccount.html')   # shows flash message and stays on current page
        #     return redirect('createAccount.html', user = failed)
        
        # # no existing accounts with provided username, create the new account
        # else:
        acctQuery = 'INSERT INTO Users (userName, userPassword, userEmail) VALUES (%s,%s,%s)'
        data = (userName, userPassword, userEmail)
        passed = execute_query(db_connection, acctQuery, data)
        flash('Your account has been created. Welcome to Ethical Eats!')

        # Note: Should we combine index_user and index_new_user or keep them separate?
        return render_template('index_new_user.html', user = passed)

@webapp.route('/continueGuest')
def continueGuest():
    return render_template("index.html")   # leads to index.html, which is the non-user index

@webapp.errorhandler(404)
def heh_error(e):
    return render_template('404.html'), 404


@webapp.errorhandler(500)
def another_heh_error(e):
    return render_template('500.html'), 500


# To start flask locally
# if __name__ == '__main__':
#     webapp.run(debug=True)
