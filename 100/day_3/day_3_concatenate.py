#Day 3 of 100 days of Python coding

#Concatenate - means to combine text (remember, text is called a string) and variables together into single sentences!
#
# It turns out print has a super-power. We can give it as many different things to print as we want. All we need to do is put a comma , between every different thing in the ().

#print(varName, "Some text")

# number = input("Give me a number: ")
# group = input("Give me a collective noun for a group of things: ")
# thing = input("Give me the name of a weird or wacky thing: ")
# print("No I don't think that", number, "is a", group, "of", thing,". That's just odd.")

#COMMON ERRORS

# INVALID SYNTAX
# yourName = input("Name: ")
# whatYear = input("What year is it?: ")
# print(yourName "thinks it is" whatYear)
#   File "main.py", line 3
#     print(yourname "thinks it is" whatYear)
#                    ^
# SyntaxError: invalid syntax
# 
# the comma is missing! - print(yourname, "thinks it is", whatYear)

# LOGIC ERROR
# yourName = input("Name: ")
# whatYear = input("What year is it?: ")
# print("yourName, thinks it is, whatYear")

# the quotes are wrong! print(yourName, "thinks it is", whatYear)
# The only thing in quotes should be the literal strings print(varName, "literal string", varName2).

#FIX MY CODE
# print("=== Your Song Generator ===")
# print("""You'll be asked a bunch of questions
# then we'll make you up an amazing
# song, totally copyright free 😭""")
# print()
# person = input("Name a person famous for something good: ")
# thing = input("Name a thing they did: ")
# place = input("Name a place you like: ")
# rhyme = input("Give me a verb that rhymes with your person's name: ")
# print()
# print("There was a person called" name)
# print("Who did something cool like", thing, "at the wonderful", place "where you'll find me", rhyme)


#FIXED CODE!
# print("=== Your Song Generator ===")
# print("""You'll be asked a bunch of questions
# then we'll make you up an amazing
# song, totally copyright free 😭""")
# print()
# person = input("Name a person famous for something good: ")
# thing = input("Name a thing they did: ")
# place = input("Name a place you like: ")
# rhyme = input("Give me a verb that rhymes with your person's name: ")
# print()
# print("There was a person called", person)
# print("Who did something cool like", thing, "at the wonderful", place, "where you'll find me", rhyme)

#REPLIT ANSWER
# print("=== Your Song Generator ===")
# print("""You'll be asked a bunch of questions
# then we'll make you up an amazing
# song, totally copyright free 😭""")
# print()

# person = input("Name a person famous for something good: ")
# thing = input("Name a thing they did: ")
# place = input("Name a place you like: ")
# rhyme = input("Give me a verb that rhymes with your person's name: ")

# print()
# print("There was a person called", person, "Who did something cool like", thing, "at the wonderful", place,  "where you'll find me", rhyme)


#DAY 3 CHALLENGE!

# We have learned enough skills for a simple, but cool, project!

# Remember when you were a kid and thought the ideal dinner would just be all your favorite things mixed in a bowl? How did that Nutella Mac & Cheese taste? Well - let's come up with a recipe generator to build us an amazing dish for today's evening meal!

# 1. Create these as a variable:
# A type of food
# A type of plant
# A method of cooking
# A word to describe burned food
# A household item 
# HINT - input is used for variables

# 2.Output a nice looking Recipe page that *concatenates* a dish in this format:
# cooking food with burned plant on a bed of item
# HINT - Think about how you use print, , and "".

#MY SOLUTION
# food = input("Name a food: ")
# plant = input("Name a plant: ")
# cooking = input("Name a method of cooking: ")
# burned = input("Whats a word that describes burned food?")
# item = input("Name any household item: ")

# print("MENU")
# print(cooking,food,"with",burned,plant,"on a bed of",item)

#REPIT ANSWER
# food = input("Name a type of food: ")
# plant = input("Name a plant: ")
# cookingType = input("What is a way to cook something?")
# burntFood = input("How do you describe burnt food?")
# householdItem = input("Name something in your house: ")

# print()
# print("Tonight's dinner:")

# print("For dinner you should make", cookingType, food, "with", burntFood, plant, "on a plate of", householdItem)
