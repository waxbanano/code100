# Day 23 of 100 days of Python coding

# Subroutine
# So far, when we wanted to repeat code, we have had to use loops or copy and paste code.

# What if I told you there was a way to use code or call it and use it anytime anywhere??

# That is a subroutine!!

# A subroutine tells the computer that a piece of code exists and to go run that code again and again...

# Just like a recipe
# Subroutines work like a recipe in a cookbook. If you want to know how to make a cake, you don't have to start from scratch every time. You can use a recipe to get the same quality each time.

# How do we define a subroutine?
# A subroutine is defined by:

# def (which stands for definition)
# You need to give the subroutine a name (and just like with a variable, you can't have spaces).



# You need to add () even if there are no arguments followed by a colon :. The code needs to be indented.

# Let's try it
# 👉 Let's roll a random number on a six-sided dice. Copy the code below and click run.

# def rollDice():
#   import random
#   dice = random.randint(1, 6)
#   print("You rolled", dice)
# Why is nothing happening??

# # In this code, I have defined how to roll a dice (this is my recipe for rolling a dice), but I have not actually 'called' the program to run.
# Call the Subroutine
# Calling the subroutine means telling it to run.

# 👉 We need to 'call' the code by adding one more line to our code with the name of the subroutine and the empty ():

# def rollDice():
#   import random
#   dice = random.randint(1, 6)
#   print("You rolled", dice)

# rollDice()
# Note that when you call the subroutine, you need to ensure you do NOT indent.

# I can even add a range and roll the dice 100 times by adding this code:

# for i in range(100):
#   rollDice()
# 👉 Try it out for yourself!

# Common Errors
# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# Name error
# 👉 Why is this code not working?

# def print My Name():
#   print("My Name is David")

# print My Name()
# Just like with variables, you cannot have spaces with subroutines (onlyCamelCase or_using_underscores).

# def printMyName():
#   print("My Name is David")

# printMyName()
# Syntax error
# 👉 What happens when you run this code? Can you spot the error?

# def countToFive:
#   for i in range(1, 6):
#     print(i)

# countToFive()
# You need to add () in the first line, even though there is no argument.

# def countToFive():
#   for i in range(1, 6):
#     print(i)

# countToFive()
# What about this one?
# 👉 Don't be fooled. This error is different than the last example.

# def countToFive():
#   for i in range(1, 6):
#     print(i)

#   countToFive()
# When you call your subroutine, make sure it is NOT indented.

# def countToFive():
#   for i in range(1, 6):
#     print(i)

# countToFive()
# Fix My Code
# 👉 Try and fix this code which is full of errors.

# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# def print favorite color:
#   print("My favorite color is red.)

#   print favorite color()
# def print_favorite_color():
#   print("My favorite color is red.")

# print_favorite_color()

# 👉 Day 23 Challenge
# Create a subroutine with both a username and password.
# Create a loop to prompt the user again and again until they put in the correct login information.

# Replit Login System

# What is your username?: david
# What is your password? whatAmazingHairYouHave

# Whoops! I don't recognize that username or password. Try again!

# What is your username? david
# What is your password? baldies4life

# Welcome to Replit!
# Create one login subroutine. Maybe you should call it login.
# Use input and if statements inside a loop.
# Where does the loop need to break? Where does it need to continue?

# 
def login():
  while True:
    username = input("what is your username: ")
    correctUserName = "Gandalf"
    password = input("what is your password: ")
    correctPassword = "#1wizard"
    if username == correctUserName and password == correctPassword:
      print("Welcome Gandalf.")
      break
    else:
      print("Try again!")
      continue

print("++++ Replit Login System")
login()


#REPLIT SOLUTION
# def login():
#   while True:
#     username = input("What is your username?: ")
#     password = input("What is your password? ")
#     if username == "David" and password == "Replit4ev#r":
#       print("Welcome David!")
#       break
#     else:
#       print("That is not the correct username or password. Try again!")
#       continue
    
# print("REPLIT LOGIN SYSTEM")
# login()