# Day 27 of 100 days of Python coding
import os, time
print("+++ Character Builder v1.00 +++")
time.sleep(2)
os.system("clear")
def characterName():
  name = input("What is the character's name?")
  return name
  
def characterType():
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
again = "yes"
while again == "yes":
  name = characterName()
  type = characterType()
  health = healthGenerator()
  strength = strengthGenerator()
  print(name,"is a",type)
  print("health:",health,)
  print("strength:",strength)
  print()
  again = input("Again? ")
  time.sleep(2)
  os.system("clear")

#REPLIT SOLUTION
#   import random, os, time

# def rollDice(side):
#   result = random.randint(1,side)
#   return result

# def health():
#   healthStat = ((rollDice(6)*rollDice(12))/2)+10
#   return healthStat

# def strength():
#   strengthStat = ((rollDice(6)*rollDice(8))/2)+12
#   return strengthStat

# while True:
#   print("⚔️ CHARACTER BUILDER ⚔️")
#   print()
#   name = input("Name your Legend:\n")
#   type = input("Character Type (Human, Elf, Wizard, Orc):\n")
#   print()
#   print(name)
#   print("HEALTH:", health())
#   print("STRENGTH:", strength())
#   print()
#   print("May your name go down in Legend…")
#   print()
#   again = input("Again?:\n")
#   if again=="No" or again=="no":
#     break
#   time.sleep(1)
#   os.system("clear")
  
  
  
  


