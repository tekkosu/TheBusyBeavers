from flask import Flask, render_template, request, url_for, session, redirect
from ethicalEats.db_connector import connect_to_database, execute_query
#from flask_mysqldb import MySQL
#import MySQLdb.cursors
import re

# Creates Flask instance
webapp = Flask(__name__)


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
    return render_template('recipebook.html', recipes=result)

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


# CONVERT THIS TO DB_CONNECT FORM LATER ON???
@webapp.route('/createAccount', methods = ['GET', 'POST'])
def createAccount():

    # check if the username, password, and email already exists in the database
    if request.method == 'POST' and 'userName' in request.form and 'userPassword' in request.form and 'userEmail' in request.form:
        # variables of user's info to reference for later
        username = request.form['userName']
        password = request.form['userPassword']
        email = request.form['userEmail']

        # check if the account exists via database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE userName = %s AND userPassword = %s', (username, password))
        acct = cursor.fetchone()

        if acct:
            msg = 'This account already exists.'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Email is invalid.'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username can only contain characters and numbers.'
        elif not username or not password or not email:
            msg = 'Please fill out the entire form to create an account.'

        # else, there is no existing account and requirements are met for user info, add new account into 'Users' Table
        else:
            cursor.execute('INSERT INTO Users VALUES (NULL, %s, %s, %s)', (username, password, email))
            mysql.connection.commit()   # DBCONNECTOR EQUIVALENT CODE???
            msg = 'Your account has been created.'

    # form is not filled out
    elif request.method == 'POST':
        msg = 'Please fill out the form to create an account.'

    return render_template('createAccount.html')   # renders createAccount.html page


@webapp.errorhandler(404)
def heh_error(e):
    return render_template('404.html'), 404


@webapp.errorhandler(500)
def another_heh_error(e):
    return render_template('500.html'), 500


# To start flask locally
# if __name__ == '__main__':
#     webapp.run(debug=True)