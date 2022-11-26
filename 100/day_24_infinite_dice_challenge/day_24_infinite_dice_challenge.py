# Day 24 of 100 days of Python coding

# Parameters
# I get it. So far, subroutines have been a bit underwhelming...

# Let's put those subroutines to better use by sending them information using parameters and making them do different things based on different inputs.

# If you change the ingredients in a recipe, you get a different kind of cake. Let's do that with subroutines.

# In a subroutine, the () are for the argument (FYI argument is another word for parameter). These are the pieces of information we pass to the code. These can be variable names that are made up for the first time within the argument ().



# Here is a simple subroutine that uses the argument to take in the name of an ingredient and expresses its opinion (quite strongly) about the ingredient that the user typed. For example, 'chocolate' is amazing, but 'broccoli'...not so much.

# 👉 Try it out.

# def whichCake(ingredient):
#   if ingredient == "chocolate":
#     print("Mmm, chocolate cake is amazing")
#   elif ingredient == "broccoli":
#     print("You what mate?!")
#   else: 
#     print("Yeah, that's great I suppose...")
# But how do we call it?

# How do we call the subroutine?
# We call it in the same way as before. However, instead of leaving the () blank, we send the code a message.



# 👉 What happens when you add this to the end of your code above?

# whichCake("chocolate")
# That's right. The variable 'ingredient' in the subroutine gets set to 'chocolate' and the output shows:



# 👉 What happens if you change "ingredient" to "broccoli"?

# Adding More Arguments
# We can have as many arguments as we want, separated by commas.



# Now, this subroutine is expecting three arguments: ingredient, base, and coating:

# def whichCake(ingredient, base, coating)
# 👉 Let's update our code to now show all three arguments:

# def whichCake(ingredient, base, coating):
#   if ingredient == "chocolate":
#     print("Mmm, chocolate cake is amazing")
#   elif ingredient == "broccoli":
#     print("You what mate?!")
#   else: 
#     print("Yeah, that's great I suppose...")
#   print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

# whichCake("carrot", "biscuit", "icing")
# 👉 I could even ask the user to name an ingredient, base, and coating by adding:

# def whichCake(ingredient, base, coating):
#   if ingredient == "chocolate":
#     print("Mmm, chocolate cake is amazing")
#   elif ingredient == "broccoli":
#     print("You what mate?!")
#   else: 
#     print("Yeah, that's great I suppose...")
#   print("So you want a", ingredient, "cake on a", base, "base with", coating, "on top?")

# userIngredient = input("Name an ingredient: ")
# userBase = input("Name a type of base: ")
# userCoating = input("Fave cake topping: ")
# whichCake(userIngredient, userBase, userCoating)
# What could you input to make a yummy cake?

# Invalid Syntax
# def biggerNumber(number1 number2):
#   if(number1 > number2):
#     print(number 1, "is bigger")
#   else:
#     print(number 2, "is bigger")

# biggerNumber (18,332)
# You need a ,. Remember, you have to add a comma in between each variable that you expect to be a parameter. You can have as many arguments as you want. Remember, though, if you create two arguments, you must also call two arguments.

# def biggerNumber(number1, number2):
#   if(number1 > number2):
#     print(number1, "is bigger")
#   else:
#     print(number2, "is bigger")

# biggerNumber (18,332)

# Fix My Code
# 👉 Try and fix this code which is full of errors.

# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# def pizza_order(topping1 topping2):
#   if topping1 = "pepperoni":
#     print(topping1, "is a great choice")
#   else:
#     print(topping1, "is kinda lame on pizza")
#   print(topping2, "sounds delicious, much better than" topping1)
  
# topping1 =  input("Name a pizza topping. ")
# topping2 = input("Name a second pizza topping. ")

#   pizza_order(topping1, topping2)
# def pizza_order(topping1, topping2):
#   if topping1 == "pepperoni":
#     print(topping1, "is a great choice")
#   else:
#     print(topping1, "is kinda lame on pizza")
#   print(topping2, "sounds delicious, much better than", topping1)
  
# topping1 =  input("Name a pizza topping. ")
# topping2 = input("Name a second pizza topping. ")

# pizza_order(topping1, topping2)

# 👉 Day 24 Challenge
# Let's build an infinity dice!

# Create subroutines that will roll a dice with any number of sides (essentially as big of a number as you like). Write one subroutine with one parameter that allows us to call a function (such as rollDice).
# Example:

# Infinity Dice 🎲

# How many sides?: 600
# You rolled 532

# Roll again? yes
# You rolled 102

# Roll again? no
# Import your library first.
# Create a variable to ask the user how many sides the dice should be.
# Create a variable that allows the user to leave the game.
# Create a subroutine with rollDice that sets the sides of the dice as the argument.
# Create a while loop that allows the user to roll again or leave the game.

##MY AWESOME SOLUTION WITH A noCheck() FUNCTION!!!!!!
import random
print("++++++++ Infinity Dice 🎲 ++++++++")
print()
sides = int(input("How many sides does the dice have? "))
rollAgain = "yes"

def rollDice(sides):
  roll = random.randint(1,sides)
  print("You rolled",roll)
  
def noCheck():
  if rollAgain == "no":
    print(" - game over - ")
    exit()
    
while rollAgain == "yes":
  rollDice(sides)
  rollAgain = input("Roll Again? ")
  noCheck()
  sides = int(input("you must be having fun, how many sides does the dice have now? "))

#REPLIT SOLUTION
# import random
# print("Infinity Dice 🎲")
  
# sides = int(input("How many sides?: "))
# playGame = "yes"
  
# def rollDice(sides):
#   print("You rolled ", random.randint(1,sides))
# while playGame == "yes":
#     rollDice(sides)
#     playGame = input("Roll again?")