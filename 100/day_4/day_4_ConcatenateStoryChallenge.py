#Day 4 of 100 days of Python coding

# DAY 4 CHALLENGE!

# Everyone loves a good story!

# Well, you're going to create your own adventure story that places your user in the role of the main character and we'll even customize the story to suit their interests.

# YOUR TASK

# 1. Ask your users to list a bunch of information about them: things they like, things they hate, names of family and friends... it's up to you how many and what kinds of things you pick. Keep it wacky!
# HINT - Think about variables and input.

# 2. Now construct your story - it can be about anything you want, but must use the variables you've created in step 1.
# HINT - Remember concatenation and the use of , and "".

# 3. Make sure to only work one paragraph at a time. Otherwise things could get a bit messy.

# EXAMPLE
# Everything which is within the curly braces {...} is what you need to ask the user, store it in a variable and then display that in your story.

# Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!

# What is your name?
# What is your worst enemy’s name?
# What is your superpower?
# Where do you live?
# What is your favorite food?

# Hello {name}! Your ability to {superpower} will make sure you never have to look at {worst enemy’s name} again. Go eat {your favorite food} as you walk down the streets of {where you live} and use {superpower} for good and not evil!

# This exact thing is how those custom books you can buy are generated - the only difference is that those are printed and shipped to your grandma for her birthday for a lot of money. Hey, maybe you can be the one charging that big price after the 100 days of code?

#DAY 4 CHALLENGE
# name = input("What is your name? ")
# enemy = input("What is your worst enemy’s name? ")
# superpower= input("What is your superpower?")
# live = input("Where do you live?")
# food = input("What is your favorite food?")

# print("Hello", (name),"!", "Your ability to", (superpower), "will make sure you never have to look at", (enemy), "again. Go eat", (food), "as you walk down the streets of", (live)," and use",(superpower)," for good and not evil!")

#@WAXBANANO DAY 4 CHALLENGE!!!!
print("\033[96m"+"==ADVENTURE QUEST 1.0==","\033[0m")
print()

name = input("What is your name? ")
print()

print("Welcome,",name+"!", "\033[96m","THE ADVENTURE QUEST BEGINS!!!!","\033[0m")
print()

land = input("Choose a place: ")
mission = input("What is your mission? ")
weapon = input("Choose a weapon type: ")
print("\n")

print("\033[96m"+"Once upon a time , in the land of",land,", Our hero",name,"uses ", weapon, "to successfully defeat the enemy and complete the mission of", mission+"!","\033[0m")
print("\n")

pet = input("What's your favorite animal? ")
monster = input("What animal are you afraid of? ")
shield = input("Name something you can't break: ")
print("\n")

print("\033[96m"+"To help you on your journey the mighty wizard has gifts for your quest! Your magical shield is made from super high strength, unbreakable",shield,". A flying",pet,"friend will help you and protect you from the",monster+"s","along the way!"+"\033[0m")
print("\n")

print("Have a safe and successfull journey",name+"!")


#COLOR CHANGING HINTS print("\033[textcolor m")
# Color	Value
# Default	0
# Black	30
# Red	31
# Green	32
# Yellow	33
# Blue	34
# Purple	35
# Cyan	36
# White	37

# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

# print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")
