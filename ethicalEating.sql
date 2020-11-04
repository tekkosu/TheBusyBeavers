DROP TABLE IF EXISTS Users, Recipes, Recipes_Users, Recipes_Ingredients, Ingredients, EthicalIngredients, Ingredients_EthicalIngredients;

CREATE TABLE Users(
userID INT(50) NOT NULL AUTO_INCREMENT PRIMARY KEY,
userName varchar(70) NOT NULL,
userPassword varchar(70) NOT NULL,
CONSTRAINT UNIQUE (userName)
) ENGINE=INNODB;

CREATE TABLE Recipes(
recipeID INT(50) NOT NULL AUTO_INCREMENT PRIMARY KEY,
recipeName varchar(50) NOT NULL
) ENGINE=INNODB;

CREATE TABLE Recipes_Users(
userID INT(50) NOT NULL,
recipeID INT(50) NOT NULL,
FOREIGN KEY (recipeID) REFERENCES Recipes (recipeID),
FOREIGN KEY (userID) REFERENCES Users (userID),
PRIMARY KEY (userID, recipeID)
) ENGINE=INNODB;

CREATE TABLE Recipes_Ingredients(
recipeID INT(50) NOT NULL,
ingredientID INT(50) NOT NULL,
FOREIGN KEY (recipeID) REFERENCES Recipes (recipeID),
FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID),
PRIMARY KEY (recipeID, ingredientID)
) ENGINE=INNODB;

CREATE TABLE Ingredients(
ingredientID INT(50) NOT NULL AUTO_INCREMENT PRIMARY KEY,
ingredientName varchar(35) NOT NULL,
ethicalIssue varchar(100)
) ENGINE=INNODB;

CREATE TABLE EthicalIngredients(
ethicalIngredientID INT(50) NOT NULL AUTO_INCREMENT PRIMARY KEY,
ingredientName varchar(35) NOT NULL,
description varchar(100)
) ENGINE=INNODB;

CREATE TABLE Ingredients_EthicalIngredients(
ethicalIngredientID INT(50) NOT NULL,
ingredientID INT(50) NOT NULL,
FOREIGN KEY (ethicalIngredientID) REFERENCES EthicalIngredients (ethicalIngredientID),
FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID),
PRIMARY KEY (ethicalIngredientID, ingredientID)
) ENGINE=INNODB;