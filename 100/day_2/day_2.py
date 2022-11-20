#Day 2 of 100 days of Python coding

#INPUT - input() is when the user gives information to the computer.
# It's very similar to the print command, except that it'll show the message in the console then wait until the user has typed something into the console and pressed enter.
#input=("whats your name?: ")

# myName = input("What's your name?: ")
# myAge = input("Whats your age?: ")
# print("Gee, thats REALLY OLD")
# replit = input("Do you like replit?")
# print("OF COURSE YOU DO!")

#VARIABLE - a variable is a value that we can use to name and store data.
#varName = input("Name >")
#underscores_between_words
#camelCaseToMakeItEasierToRead

# print()
# print("So, you are")
# print(myName)
# print("and are the ripe old age of")
# print(myAge)
# print("and clearly think that Replit is")
# print(replit)


#FIX MY CODE#

#SYNTAX ERROR#

# my variable = input("WHO GOES THERE? ")
# print(my variable)

#  File "main.py", line 1
#     my variable = input("WHO GOES THERE? ")
#        ^
# SyntaxError: invalid syntax

# myvariable = input("WHO GOES THERE? ")
# print(myvariable)

# space in the variable name (myvariable) caused the syntax error.

#NAME ERROR#

# myGrandma = input("How's your Grandma doing? 😘 ")

# print(mygrandma)

# How's your Grandma doing? 😘 fine
# Traceback (most recent call last):
#   File "main.py", line 2, in <module>
#     print(mygrandma)
# NameError: name 'mygrandma' is not defined

# myGrandma = input("How's your Grandma doing? 😘 ")
# print(myGrandma)

# variable names didnt match(myGrandma & mygrandma)

#LOGIC ERROR#

# myLunch = input("What are you having for lunch? ")
# print("Hmm, it sounds like you really should just order")
# print("myLunch")
# print("as soon as possible!")

# myLunch was put in quotes making it a string, so it wasnt called as a variable. it's printing the variable name instead of the contents of the variable.

# myLunch = input("What are you having for lunch? ")
# print("Hmm, it sounds like you really should just order")
# print(myLunch)
# print("as soon as possible!")

#FIX MY CODE#

# print("Definitely not a Phishing Scam")
# print()
# input("Your Name")
# print("Thanks for logging in")
# print(myName)
# cardNumber = input("What is your credit card number?")
# print("Thanks, I definitely wont put")
# print("cardNumber")
# print("into Amazon and order anything weird")
# print()
# print("Promise")
# maidenName input("What is your Mother's maiden name? ")
# print()
# print("That's cool, I just wanted to know that")
# print(maidenName)
# print("was your Mum's maiden name. Not because the bank requested it or anything, honest.")

#MY ANSWER 
# print("Definitely not a Phishing Scam!!")
# print()
# myName = input("Your Name: ")
# print("Thanks for logging in")
# print(myName)
# cardNumber = input("What is your credit card number? ")
# print("Thanks, I definitely wont put")
# print(cardNumber)
# print("into Amazon and order anything weird!")
# print()
# print("Promise!")
# maidenName = input("What is your Mother's maiden name? ")
# print()
# print("That's cool, I just wanted to know that")
# print(maidenName)
# print("was your Mum's maiden name. Not because the bank requested it or anything, honest.")

#REPLIT ANSWER
# print("Definitely not a Phishing Scam")
# print()
# myName = input("What is your name?")
# print("Thanks for logging in")
# print(myName)
# cardNumber = input("What is your credit card number?")
# print("Thanks, I definitely won't put")
# print(cardNumber)
# print("into Amazon and order anything weird")
# print()
# print("Promise")
# maidenName = input("What is your Mother's maiden name? ")
# print()
# print("That's cool, I just wanted to know that")
# print(maidenName)
# print("was your Mum's maiden name. Not because the bank requested it or anything, honest.")

#DAY 2 CHALLENGE!
# 1.Asks for the user's name, favorite food, favorite music and where they live (or you can create other questions!)


# I WANTED TO DO TODAYS CHALLENGE IN SPANISH SINCE I AM LEARNING BOTH!
user_name = input("¿Cuál es su nombre? ")
print("Hola")
print(user_name)
print()
favorite_food = input("¿Cuál es tu comida favorita? ")
print(favorite_food)
print("¡Muy bueno!")
print()
favorite_music = input("¿Cuál es tu música favorita? ")
print("¡Excelente!")
print()
home = input("¿Donde vives? ")
print("¡Maravilloso!")
print()
print("¡Tu comida favorita es la")
print(favorite_food)
print(":)")
print()
print("¡Tu música favorita es la")
print(favorite_music)
print(":)")
print()
print("¡Vives en ")
print(home)
print(":)")


#SOLUTION
# print("Getting to know you!")

# YourName = input("What is your name?")
# Hungry = input ("What is your favorite food?")
# Music = input("What is your favorite music?")
# WhereAreYou = input("Where are you?")

# print("You are")
# print(YourName)
# print() 

# print("You're probably hungry for")
# print(Hungry)
# print()
# print("You're probably listening to")
# print (Music)
# print()
# print ("You're probably living in the amazing")
# print (WhereAreYou)
# print() 
# print ("Have a great day!")