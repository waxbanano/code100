#Day 5 of 100 days of Python coding

# If Statements
# These statements are a bit like asking a question. You are telling the computer: if something is true, then do this specific block of code. Double equals (==) is asking the computer to compare if these two things are exactly the same.

 

# In the code below, I am asking if the variable myName is the same as the string David.

# myName = input("What's your name?: ")
# if myName == "David":
# But that doesn't print anything?
# To create a print statement related to the input from the if statement, you must go to the next line and indent once (Luckily, Replit does this for you, but be careful!) so it is all a part of the code we run.

# 👉 Copy this code and see what happens.

# myName = input("What's your name?: ")
# if myName == "David":
#   print("Welcome Dude!")
# What is else?
# If the condition is not met with the if statement, then we want the computer to do the else part instead. Likewise, if the condition is met in the if statement, then the else bit is ignored by the computer. The else statement must be the first thing unindented after the if statement and in line with it (Replit helps you out here too!)

# 👉 Copy this code and give it a go. Watch those indents!

# myName = input("What's your name?: ")
# if myName == "David":
#  print("Welcome Dude!")
#  print("You're just the baldest dude I've ever seen")
# else:
#  print("Who on earth are you?!")


# Common Errors
# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# Syntax Error
# 👉 What is wrong with this code below?

# catsOrDogs = input("Are you a cat person? Or a dog person?: ")
# if catsOrDogs = "cat":
#   print("Meow")
# else:
#   print("Woof")

#   Our if statement must include == so it should read:
# if catsOrDogs == "cat":

# Syntax Error...again
# 👉 What is wrong with this code?

# catsOrDogs = input("Are you a cat person? Or a dog person?: ")
# if catsOrDogs == "cat"
#   print("Meow")
# else:
#   print("Woof")
# Our if statement is missing the :

# Indentation Error
# 👉 Do you see the error here?

# catsOrDogs = input("Are you a cat person? Or a dog person?: ")
# if catsOrDogs == "cat":
#   print("Meow")
# else:
# print("Woof")
# As soon as you see a colon, the next line should be indented one more than the line above it.

# Fix My Code
# drink = input("Do you prefer coffee or tea?)
# if drink = "coffee"
#   print("Tea is better.")
#     else:
#   print("Excellent choice.")

#FIXED!
# drink = input("Do you prefer coffee or tea?")
# if drink == "coffee":
#   print("Tea is better.")
# else:
#   print("Excellent choice.")


####
#input will NOT TAKE COLORS and Formatted string literals must be used, (f-strings) let us include expressions inside of a string by prefixing the string with f.

# variable = 'language'

# user_input = input(f'Enter your preferred {variable}: ')

# print(user_input)
####

##DAY 5 IF ELSE EXCERCISE
# myTitle = ("""
#     if:
#   else:
#   """)
# print("\033[3m",myTitle, "\033[0m")
# print("\n")
# who = "\033[34m"+"Who goes there?! "
# whoGoesThere = input(f'{who}')
# print("\n")

# youShallNotPass = "\033[31m"+" YOU SHALL NOT PASS!!! "
# noPassCenter = youShallNotPass.center(40,"💀")

# if whoGoesThere == "Gandalf":
#   print("\033[93m","\U0001F31F","You Shall Pass!","\U0001F31F","\033[0m")
# else: 
#   print(noPassCenter)

# 👉 Day 5 Challenge
# "Which character are you?" Generator
# You will need to:

# Ask your users a series of questions that identify if they're one of the characters in the world you have created.
# Organize your questions and potential answers before you start to more easily identify how to code it.

# Add multiple if statements to check the result of each question.
# Use input and variables to ask the questions, but ask each question only before the next if statement.

# Make sure to have a final print if they haven't selected any of the characters so far.
# else

# Example
# Marvel Movie Character Creator
# --
# Do you like 'hanging around'?: No
# Then you're not Spider-man

# Do you have a 'gravelly' voice?: No
# Aww, then you're not Korg

# Do you often feel 'Marvelous'?: Yes
# Aha! You're Captain Marvel! Hi!

# @WAXBANANO DAY 5 CHALLENGE!!!!!!!!
# WHAT POLITICAL PARTY ARE YOU?!

# QUESTONS:
# Do you think guns should be banned?
#   then you're probobaly not a republican! 
#   Most likely you voted as a democrat!

# Do you think abortion should be banned?
#     then you're probobaly not a democrat! 
#     Most likely you voted as a republican!

# Are you a republican?

# Are you a Democrat?

# Is your name Donald Trump?

# ANSWERS:

# RED:
noBlue = "\033[31m"+"Then you're probobaly not a democrat!"+"\033[0m"
yesRed= "\033[31m"+"*** Most likely you voted as a republican! ***"+"\033[0m"

# # BLUE:
yesBlue = "\033[94m"+"*** Most likely you voted as a democrat! ***"+"\033[0m"
noRed= "\033[94m"+"Then you're probobaly not a republican!"+"\033[0m"

# # TITLE
print("\033[94m"+"**********"+"\033[0m"+" POLITICAL PARTY QUIZ 1.0 "+"\033[31m"+"**********"+"\033[0m")
print()
print("Which USA political Party do you support?")
print()
print("Answer these questions and let's find out!")
print()
print("Please use yes and no for your answers.")
print("\n")

# 1ST QUESTION
guns = input("Do you think guns should be banned? --> ")
print("\n")

if guns == "yes":
  print(yesBlue)
else:
  print(yesRed)
print("\n")

# 2ND QUESTION
baby = input("Do you think abortion should be banned? --> ")
print("\n")

if baby == "yes":
  print(yesRed)
else:
  print(yesBlue)
print("\n")

# 3RD QUESTION
red = input("Are you a republican? --> ")
print("\n")

if red == "yes":
  print(noBlue)
else:
  print(noRed)
print("\n")

# 4TH QUESTION
red = input("Are you a democrat? --> ")
print("\n")

if red == "yes":
  print(noRed)
else:
  print(noBlue)
print("\n")

# 5TH QUESTION
red = input("Are you Donald Trump? --> ")
print("\n")

if red == "yes":
  print(noBlue)
else:
  print(noRed)
print("\n")

print("*PLEASE WAIT* ANALYZING RESULTS....... ")
print("\n")





#REPLIT SOLUTION
# print("Which character are you from 'Avengers?'")
# print()
# print("Answer these questions and let's find out.")
# print()
# print("Please use Y or N for yes and no.")

# likeGreen = input("Do you like the color green?: ")
# if likeGreen == "Y":
#   print("You must be the Hulk!")

# IronIsCool = input("Do you think building robots is cool?: ")  
# if IronIsCool == "Y":
#   print("You must be Iron Man. Cool suit!")

# TimeTravel = input("Do you like traveling through time?: ")  
# if TimeTravel == "Y":
#   print("You must be Captain America!")

# Strong = input("Are you super strong?: ")
# if Strong == "Y":
#   print("You have got to be Thor!")
# else:
#   print("I guess you are not like anyone from 'Avengers.'")