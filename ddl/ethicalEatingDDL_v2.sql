DROP TABLE IF EXISTS Ingredients_EthicalIngredients, EthicalIngredients, Recipes_Ingredients, Ingredients, Recipes_Users, Recipes, Users;

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

CREATE TABLE Ingredients(
ingredientID INT(50) NOT NULL AUTO_INCREMENT PRIMARY KEY,
ingredientName varchar(35) NOT NULL,
ethicalIssue BOOLEAN,
ethicalDescription varchar(200)
) ENGINE=INNODB;

CREATE TABLE Recipes_Ingredients(
recipeID INT(50) NOT NULL,
ingredientID INT(50) NOT NULL,
FOREIGN KEY (recipeID) REFERENCES Recipes (recipeID),
FOREIGN KEY (ingredientID) REFERENCES Ingredients (ingredientID),
PRIMARY KEY (recipeID, ingredientID)
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

-- Insertion statements for sample DB data
INSERT INTO `Users` (`userID`, `userName`, `userPassword`) VALUES
(1, 'holtze', 'password'),
(2, 'tekk', 'strongpassword'),
(3, 'jensenj', 'p@ssword'),
(4, 'yehl', 'strongp@ssword1');


INSERT INTO `Recipes` (`recipeID`, `recipeName`) VALUES
(1, 'Omelette'),
(2, 'Chicken Noodle Soup'),
(3, 'Mac-n-Cheese');

INSERT INTO `Recipes_Users` (`userID`, `recipeID`) VALUES
(1, 1),
(1, 3),
(2, 2),
(3, 2),
(4, 1),
(4, 3);


INSERT INTO `Ingredients` (`ingredientID`, `ingredientName`, `ethicalIssue`, `ethicalDescription`) VALUES
(1, 'Egg', TRUE, 'Animal Product. If animal product averse, seek alternative.'),
(2, 'Mushrooms', FALSE, ''),
(3, 'Cheese', TRUE, 'Animal Product. If animal product averse or lactose intolerant, seek alternative.'),
(4, 'Pasta Noodles', FALSE, ''),
(5, 'Chicken', TRUE, 'Animal Product. If animal product averse, seek alternative.'),
(6, 'Carrots', FALSE, '');

INSERT INTO `Recipes_Ingredients` (`recipeID`, `ingredientID`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(2, 6),
(3, 3),
(3, 4);

INSERT INTO `EthicalIngredients` (`ethicalIngredientID`, `ingredientName`, `description`) VALUES
(1, 'Chickpeas', 'Chickpeas are a substitute for Chicken.'),
(2, 'Vegan Cheese Replacement', 'Use vegan cheese replacement made from coconut and potato.'),
(3, 'Just Egg', 'Just Egg is an eggless replacement for scrambled eggs made from Fava Beans.');

INSERT INTO `Ingredients_EthicalIngredients` (`ethicalIngredientID`, `ingredientID`) VALUES
(1,5),
(3,1),
(2,3);

