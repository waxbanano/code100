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
print("+++ Character Battle v1.00 +++")
time.sleep(2)
os.system("clear")
def rollDice(sides):
  import random
  roll = random.randint(1,sides)
  return roll
  
def health():
  roll_6 = rollDice(6)
  roll_8 = rollDice(8)
  health = ((roll_6*roll_8)/2)+10
  return health
  
def strength():
  roll_6 = rollDice(6)
  roll_8 = rollDice(8)
  strength = ((roll_6*roll_8)/2)+12
  return strength
# def roundChar1():
#   round1 = rollDice(6)
#   return round1
# def roundChar2():
#   round2 = rollDice(6)
#   return round2
# def roundWinner():
#   roundChar1 = roundChar1()
#   roundChar2 = roundChar2()
  
print("+++ Character Battle v1.00 +++")
    
name1 = input("What is the name of character 1? ")
type1 = input("What is the type of character 1? ")
print(name1,"is a",type1)
name1health = health()
name1strength = strength()
print("health:",name1health,)
print("strength:",name1strength)
print()
print("who are they battling? ")
name2 = input("What is character 2's name?")
type2 = input("What is character 2's type? ")
print(name2,"is a",type2)
name2health = health()
name2strength = strength()
print("health:",name2health,)
print("strength:",name2strength)
print()
#battle
round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")
  print("The battle begins")

  c1roll = rollDice(6)
  c2roll = rollDice(6)
  difference = abs(name1strength - name2strength) + 1

  if c1roll > c2roll:
    name2health -= difference
    if round == 1:
      print(name1, "wins the first round")
      time.sleep(2)
    else:
      print(name1, "wins wound")
      time.sleep(2)
  elif c2roll > c1roll:
    name1health -= difference
    if round == 1:
      print(name2,"wins the first round")
      time.sleep(2)
    else:
      print(name2, "wins round")
      time.sleep(2)
  else:
    print("round",round,"draw")
  print(name1)
  print("health:",name1health)
  print(name2)
  print("health:",name2health)

  if name1health <= 0:
    print(name1, "has died!")
    time.sleep(3)
    winner = name2 
    break
  elif name2health <= 0:
    print(name2, "has died!")
    time.sleep(3)
    winner = name1
    break
  else:
    print("And they're both standing for the next round")
    round += 1
    time.sleep(4)
    

time.sleep(1)
os.system("clear")
print()
print(winner, "has won in", round, "rounds")
