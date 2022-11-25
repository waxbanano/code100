# Day 22 of 100 days of Python coding

# Libraries
# Libraries are collections of code that other people have written. Video games often use massive libraries (for example: game engines) to create the epic water reflections, 3-D graphics, etc.

# We are going to start a bit smaller by just generating random numbers. (After all, random numbers are the basis of most games).

# Random library
# We can use a library by writing import and then the library name.

# This should always be one of the first lines of code.

# 👉 Let's import a library that will generate random numbers: (Does this look familiar from Day 14's Rock, Paper, Scissors game?)


# import random
# How random works
# In the code below, I have created a variable, 'myNumber'. I am making it equal to a random number given to me by the randint (random integer) library. I add the lowest number (1) and the highest number (100) that can be picked and the computer will generate a number at random.

# import random
# myNumber = random.randint(1,100)
# print(myNumber)
# 👉 Give it a try!

# What do I do with libraries?
# In the past, we had to hardcode the value users were looking for (remember the higher or lower guessing game...).

# With random, we can generate a number that even we don't know. (Sounds similar to gaming, huh?)

# Common Errors
# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# Name Error
# 👉 Why is this code showing the error of "name not defined?"

# import random

# myNumber = randint(1, 100)
# print(myNumber)
# Error with random numbers and loops
# 👉 For this code, I want 10 random numbers between 1-100 printed out. Why is it printing the same number instead of ten different random numbers?

# import random

# myNumber = random.randint(1, 100)
# for i in range(10):
#   print(myNumber)
# The problem is when I am generating my random number, I am doing it before the loop. I am asking for one random number and then storing it in a variable. Then, I am saying to print out this random number 10 times. Nowhere in the loop am I asking for a new number each time. I need to rearrange the order of my code.

# import random

# for i in range(10):
#   myNumber = random.randint(1, 100)
#   print(myNumber)
# Now, each time the loop resets, it will generate a new random number. Now I can generate 10 random numbers between 1-100.

# Common Errors
# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# Name Error
# 👉 Why is this code showing the error of "name not defined?"

# import random

# myNumber = randint(1, 100)
# print(myNumber)
# Error with random numbers and loops
# 👉 For this code, I want 10 random numbers between 1-100 printed out. Why is it printing the same number instead of ten different random numbers?

# import random

# myNumber = random.randint(1, 100)
# for i in range(10):
#   print(myNumber)
# The problem is when I am generating my random number, I am doing it before the loop. I am asking for one random number and then storing it in a variable. Then, I am saying to print out this random number 10 times. Nowhere in the loop am I asking for a new number each time. I need to rearrange the order of my code.

# import random

# for i in range(10):
#   myNumber = random.randint(1, 100)
#   print(myNumber)
# Now, each time the loop resets, it will generate a new random number. Now I can generate 10 random numbers between 1-100.

# 👉 Day 22 Challenge
# Copy and paste your code from Day 18.

# We are going to make a change to this project:

# Make the number generator completely random between 1 and 1,000,000. Now, the game will always have the user guess a random number each time (now the user can't cheat...)

# Totally Random One-Million-to-One

# What is your guess?: 500000
# Too low

# What is your guess?: 750000
# Too high

# What is your guess?: 600000
# Too low

# What is your guess?: 650000
# Correct!

# It took you 4 guesses to get the number correct.
# Click 'run' to try again with a different number.
# Remember to import your library first and do NOT add it in the loop.
# You can keep a lot of Day 18's code, but need to add the random library.

import random
print("+++ GUESS THE NUMBER! v2.0 +++")
print("Can you guess what number i'm thinking of?")
print()
setTheNumber = random.randint(1,10)
tries = 1
while True:
  guess = int(input("Guess a number between 1 and 10 -->"))
  if guess == setTheNumber:
    print("Correct!","It took you",tries,"tries to guess my number which was",setTheNumber,)
    exit()
  elif guess <= 0:
    print("ERROR: TOO MEGATIVE!!! EXITING PROGRAM")
    exit()
  elif guess > 1000000:
    print("choose a number between 1 and 1000000")
    tries +=1
  elif guess < setTheNumber:
    print("Thats not the number i was thinking of, try a higher number.")
    print()
    tries +=1
    continue
  elif guess > setTheNumber:
    print("Thats not the number i was thinking of, try a lower number.")
    print()
    tries +=1
    continue
