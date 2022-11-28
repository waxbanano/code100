# Day 28 of 100 days of Python coding
# 👉 Day 28 Challenge
# Use Day 27's character generator for this project...to build an automated game battle system!

# Add return functions to your character's health and strength statuses from Day 27's project.
# Generate two different characters and store their data (health and strength stats, character type, name, etc.).
# Use a while True loop to simulate those two characters battling.
# Roll one six-sided dice for both characters. The character who rolls the higher amount wins that round.
# The winner of that round (the one who rolled the higher number) will give damage to the other character by doing the following:
# Find the difference between the strength of both opponents and add one.
# Take that amount away from the loser's health.
# At the end of each round, check the stats of each character to ensure neither of them have died yet.
# When one character dies (they run out of health), declare a winner of the battle!
# To keep this battle from looking hideous between rounds use time.sleep to pause between rounds os.system("clear") to ensure the screen clears between battles.
# Extra points for the use of emojis, colors, or even sound code!

# Example:

# ⚔️ BATTLE TIME ⚔️

# Name your Legend:
# Arthur the Magnificent
# Character Type (Human, Elf, Wizard, Orc): 
# Elf

# Arthur the Magnificent
# HEALTH: 13
# STRENGTH: 18

# Who are they battling?

# Name your Legend:
# Sheila the Almighty
# Character Type (Human, Elf, Wizard, Orc): 
# Human

# Sheila the Almighty
# HEALTH: 40
# STRENGTH: 26

# *clear screen here*

# ⚔️ BATTLE TIME ⚔️

# The battle begins!

# Arthur wins the first blow
# Sheila takes a hit, with 8 damage

# Arthur the Magnificent
# HEALTH: 13

# Sheila the Almighty
# HEALTH: 32

# And they're both standing for the next round!

# *clear screen here*

# ⚔️ BATTLE TIME ⚔️

# The battle continues!

# Sheila wins round 2
# Arthur takes a hit, with 8 damage

# Arthur the Magnificent
# HEALTH: 5

# Sheila the Almighty
# HEALTH: 32

# And they're both standing for the next round!

# *clear screen here*

# ⚔️ BATTLE TIME ⚔️

# The battle continues!

# Sheila wins round 3
# Arthur takes a hit, with 8 damage

# Arthur the Magnificent
# HEALTH: -3

# Sheila the Almighty
# HEALTH: 32

# Oh no Arthur the Mighty has died!

# Sheila the Almighty destroyed Arthur the Magnificent in 3 rounds!
# Start with the code you created from Day 27.
# Keep the same subroutines as Day 27 and add one more subroutine about character damage (how a winner is declared in each round).
# Tweak the while loop from Day 27 to introduce the first character and their stats followed by the character they will battle and that character's stats. (You will want to include pausing and clearing of the code as you did on Day 27).
# Create a counter (within the loop) to keep track of the winner for each round.
# Create another while loop inside the current while loop with if statements, pausing, and clearing of code to show what happens if character 1 wins, the characters tie, etc.
# Make sure you give a recap of the health each character has left after each round.

import os, time
print("+++ Character Builder v1.00 +++")
time.sleep(2)
os.system("clear")
def characterName():
  name = input("What is character 1's name?")
  return name
def character2Name():
  name = input("What is character 2's name?")
  return name  
  
def characterType():
  type = input("What is the character's type?")
  return type
def character2Type():
  type = input("What is the character's type?")
  return type  
  
def rollDice(sides):
  import random
  roll = random.randint(1,sides)
  return roll
  
def healthGenerator():
  roll_6 = rollDice(6)
  roll_8 = rollDice(8)
  health = ((roll_6*roll_8)/2)+10
  return health
  
def strengthGenerator():
  roll_6 = rollDice(6)
  roll_8 = rollDice(8)
  strength = ((roll_6*roll_8)/2)+12
  return strength
def roundChar1():
  round1 = rollDice(6)
  return round1
def roundChar2():
  round2 = rollDice(6)
  return round2
def roundWinner():
  roundChar1 = roundChar1()
  roundChar2 = roundChar2()

alive = "yes"
while alive == "yes":
  name = characterName()
  type = characterType()
  name2 = character2Name() 
  type2 = character2Type()
  health = healthGenerator()
  strength = strengthGenerator()
  health2 = healthGenerator()
  strength2 = strengthGenerator()
  print(name,"is a",type)
  print("health:",health,)
  print("strength:",strength)
  print()
  print(name2,"is a",type2)
  print("health:",health2,)
  print("strength:",strength2)
  damage = abs(strength - strength2)+1
  
  while alive == "yes":
    roundChar1 = roundChar1()
    roundChar2 = roundChar2()
    if roundChar1 > roundChar2:
      print(characterName,"won")
      strength2-damage
    elif roundChar2 > roundChar1:
      print(name2,"won")
      strength = damage-int(strength)
    elif roundChar1 == roundChar2:
      print("tie")
    elif strength < 1 or strength2 < 1:
      alive = "no"
      print("dead")

    
  
  


    
  again = input("Again? ")
  time.sleep(2)
  os.system("clear")

