#Day 7 of 100 days of Python coding

# Nesting
# Nesting is where we put an if statement within an if statement using the power of indenting. The second if statement within the first if statement must be indented and its print statement needs to be indented one more time.

# 👉 Do you notice the second if statement below about faveCharacter and how it is indented?

# tvShow = input("What is your favorite tv show? ")
# if tvShow == "peppa pig":
#   print("Ugh, why?")
#   faveCharacter = input("Who is your favorite character? ")
#   if faveCharacter == "daddy pig":
#     print("Right answer")
#   else:
#     print("Nah, Daddy Pig's the greatest")
# elif tvShow == "paw patrol":
#   print("Aww, sad times")
# else:
#   print("Yeah, that's cool and all…")
# I highly doubt your favorite TV shows are Peppa Pig and Paw Patrol. Copy the code above and change it to match your favorite TV shows and characters.

#MY SHOWS!
# tvShow = input("What is your favorite TV show? ")
# if tvShow == "Mr. Robot":
#   print("Good choice!")
#   faveEpisode = input("What's your favorite episode? ")
#   if faveEpisode == "any":
#     print("yes definitely!")
#   else:
#     print("sure, maybe")
# elif tvShow == "Shameless":
#   print("you're dirty, i like it!")
#   faveCharacter = input("Who's your favorite character? ")
#   if faveCharacter == "Frank":
#     print("eww gross")
#   else:
#     print("they are great")
# else:
#   print("never heard of it...")

# Syntax Error
# 👉 What is wrong with the code below?

# tvShow = input("What is your favourite tv show? ")
# if tvShow == "peppa pig":
#   print("Ugh, why?")
#   faveCharacter = input("Who is your favourite character? ")
#   if faveCharacter == "daddy pig":
#     print("Right answer")
# else:
#   print("Nah, Daddy Pig's the greatest")
# elif tvShow == "paw patrol":
#   print("Aww, sad times")
# else:
#   print("Yeah, that's cool and all…")
# else:
#   print("Nah, Daddy Pig's the greatest")
# is not indented properly.

# This else statement is referring to faveCharacter and therefore, both the above else and print statements need to be indented one time. Highlight them both and click 'tab' one time.

# Fix My Code
# order = input(What would you like to order: pizza or hamburger? ")
# if order = "hamburger":
# print("Thank you.")
#   cheese = input("Do you want cheese?")
#   if cheese == "yes":
#   print("You got it.")
# else: 
#     print("No cheese it is.")
# elif order == pizza:
#   print("Pizza coming up.")
#   toppings = input("Do you want pepperoni on that?")
#   if toppings = "yes"
#     print("We will add pepperoni.")
# else:
#   print"Your pizza will not have pepperoni.")

#FIXED
# order = input("What would you like to order: pizza or hamburger? ")
# if order == "hamburger":
#   print("Thank you.")
#   cheese = input("Do you want cheese?")
#   if cheese == "yes":
#     print("You got it.")
#   else: 
#     print("No cheese it is.")
# elif order == "pizza":
#   print("Pizza coming up.")
#   toppings = input("Do you want pepperoni on that?")
#   if toppings == "yes":
#     print("We will add pepperoni.")
# else:
#   print("Your pizza will not have pepperoni.")

# 👉 Day 7 Challenge
# Fake Fan Question Generator
# Wanna find out if someone else is a true superfan of the same show, movie or interest as you? Create a program that asks what someone is interested in and includes nested if statements to ask annoying follow-up questions to see if someone is the real deal!

# Make sure you include multiple if/elif statements and nested if statements too!

# The code from today is a good place to get you started.

tvShow = input("What is your favorite TV show? ")
if tvShow == "Mr. Robot":
  print("Good choice!")
  faveEpisode = input("What's your favorite episode? ")
  if faveEpisode == "any":
    print("yes definitely!")
  else:
    print("sure, maybe")
elif tvShow == "Shameless":
  print("you're dirty, i like it!")
  faveCharacter = input("Who's your favorite character? ")
  if faveCharacter == "Frank":
    print("eww gross")
    whyHim = input("BUT WHY HIM?! ")
    if whyHim == "i dont know":
      print("oh ok")
    else:
      print("damn")
  elif faveCharacter == "Fiona":
    print("She's Great!")
  elif faveCharacter == "Lip":
    print("a cool dude, definitely!")
  elif faveCharacter == "Carl":
    print("what a badass!")  
  else:
    print("they are great")
else:
  print("never heard of it...")

  
# SOLUTION REPLIT
# print ("Are you a superfan of 'The Big Bang Theory' or a fake fan?")
# print()
# print("Answer these questions to find out.")

# Glasses = input("Does someone wear glasses?")
# if Glasses == "yes":
#   print("Correct!")
# else:
#   print("Wrong!")
#   WhoGlasses = input("And who wears glasses?")
#   if WhoGlasses == "Leonard":
#     print("You got it")
#   else:
#     print("Try again!")