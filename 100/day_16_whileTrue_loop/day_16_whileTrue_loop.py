# Day 16 of Python 100 days of code
# 👉Let's try it out.
# What do you think the below code does?

# Remember you can use the big Stop button on the top if your program does not end.

# while True:
#   print("This program is running")
# print("Aww, I was having a good time 😭")
# This type of loop only has two conditions: True and False. Make note of the capital "T" and "F".

# A Boolean Loop has two values: True or False. Impress your friends and tell them you know how to use a Boolean Loop.
# In this loop, I am saying to the computer:

# "while True is True...do this over and over again."

# Yes, we made an infinite loop, but hold on...

# Make it stop
# There is a way to stop the loop with the word break. This exits the loop and stops all code at that point. Even if there is more code written after break that is inside the loop.

# After break, the computer jumps out of the loop to the next unindented line of code.



# 👉 Let's try it out
# Run the code below and notice how the loop will continue until break. Then the next line of unindented code will run.

# while True:
#   print("This program is running")
#   goAgain = input("Go again?: ")
#   if goAgain == "no":
#     break
# print("Aww, I was having a good time 😭")

# while True:
#   print("while true boolean loop running "*50000)
#   goAgain = input("Go again?: ")
#   if goAgain =="no":
#     break
# print("awww, i was having a good time")

# Name Error
# 👉 What is the error here?

counter = 0
# while true:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
#   addAnother = input("Add another? ")
#   if addAnother == "no":
#     break
# print("Bye!")

# while true needs to be while True.

# Notice when you change the lowercase "t" to a capital "T", the color of the word changes as Replit is now recognizing this as a Boolean loop.

# Syntax Error
# 👉 What about this one? What happens when you hit run?

# counter = 0
# while True:
#   answer = int(input("Enter a number: "))
#   print("Adding it up!")
#   counter += answer
#   print("Current total is", counter)
# addAnother = input("Add another? ")
# if addAnother == "no":
#   break
# print("Bye!")

# Notice the error message is saying the syntax error "break outside loop". Do you notice how the last three lines before the bottom print statement are not a part of the loop as they are not properly indented (look at the vertical lines)?

# Highlight these three lines of code and press tab key one time to indent this code so it is inside the loop.

# Fix My Code
# 👉 Try and fix this code which is full of errors.

# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#     break
#   else:
#     print("Cool color!")
# print("I don't like red")

# The word 'true' needs to be capitalized for a while True loop.
# The if statement needs ==.
# There is an indention error with break.

# 👉 Day 16 Challenge
# Create a "Name the Lyrics" game. Write your favorite song lyrics with a word or two missing. The user has to figure out the correct song lyric in as few attempts as possible. Find the true lyric master among you!

# Example
# Fill in the blank lyrics!
# (Type in the blank lyrics and see if you are as cool as me.)

# Never going to ______ you up.
# put
# Nope, try again.

# Never going to ______ you up.
# let
# Nope, try again.

# Never going to ______ you up.
# give

# Well done! It only took you 3 attempts.
# Think of your while True loop as a replacement for the if statement.
# Place your break after the code identifying the correct lyric answer.

print("+++ Name the lyrics game +++")
print("Fill in the blank lyrics!")
print()
print("Never going to ____ you up.")
print()
count = 1
while True:
  guess = input("what's the missing lyric? --> ")
  print()
  if guess == "give" and count == 1:
    print("Correct!")
    print("You got it on your first try! Never going to give you up!")
    break
  elif guess == "give":
    print("Correct!")
    print("It only took you",count,"attempts!")
    break
  else:
    print("guess again!")
    count +=1
    print()



# REPLIT SOLUTION

# print("Welcome to Name the Song Lyric")
# print()
# print("Figure out the missing word as quickly as you can!")
# print()

# counter = 1
# while True:
#   lyrics = input("I don't wanna ______ a thing. ")
#   if lyrics == "miss" or lyrics == "Miss":
#     print("You got it!")
#   else:
#     print("Nope! Try again!")
#     counter +=1
#   if lyrics == "miss":
#     break
# print("Thanks for playing!")

# print("You got the correct lyrics in", counter, "attempt(s).")