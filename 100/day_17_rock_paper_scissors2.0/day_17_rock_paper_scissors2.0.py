
# day 17 of 100 days of Python coding

# Another Cheat
# So far we've used break in the while True loop. break leaves the loop completely and runs the next unindented line of code. However, you may want to stop the code and start the loop from the top again. (This is ideal for building games!)



# In the code below, the game runs and the user is asked if they want to go left or right. If the user chooses left, they fall to their death, and break will kick the user out of the loop. That's the game.

# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
# Well that's a bit lame and not any different than what we learned in day 16...now for the cheat.

# The Continue Command
# The continue command stops executing code in the loop and starts at the top of the loop again. Essentially, we want to kick the user back to the original question.



# Adding continue will start the code from the start and ask the first question again: "Do you go left or right?".

# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
# The else statement refers to any input besides left or right (up or esc). Since the user is a winner, we do not want to use break or it would say they have failed.

# So how do we make it stop?

# while True:
#   print("You are in a corrider, do you go left or right?")
#   direction = input("-> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit()
# print("Game Over")

# Common Errors
# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# 👉 What is wrong here?

# while True:
#   print("You are in a corridor, do you go left or right?")
#   direction = input("> ")
#   if direction == "left":
#     print("You have fallen to your death")
#     break
#   elif direction == "right":
#     continue
#   else:
#     print("Ahh! You're a genius, you've won")
#     exit
# print("The game is over, you've failed!")

# Fix My Code
# 👉 Try and fix this code which is full of errors.

# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# print("Let's play chutes and ladders. Pick ladder or chute.")
# while True:
#   print("Do you want to go up the ladder or down the chute?")
#   direction = input("> ")
#   if direction == "chute":
#     print("Game over!")
#     break
#   elif direction == "ladder":
#     continue
#   else:
#     print("Game over!")
#     exit()
# print("Thanks for playing!")

# print("Let's play chutes and ladders. Pick ladder or chute.")
# ladderCount = 0
# while True:
#   print("Do you want to go up the ladder or down the chute?")
#   direction = input("> ")
#   if direction == "chute":
#     print("Game over!")
#     break
#   elif direction == "ladder":
#     ladderCount +=1
#     print(ladderCount)
#     continue
#   else:
#     print("Game over!")
#     exit ()
# print("Thanks for playing!")

# 👉 Day 17 Challenge
# Go find your Rock, Paper, Scissors game from Day 14 and add the code here before you start. We are going to build upon this game.

# Use a loop to repeat the game multiple rounds.
# Keep score of player 1 and player 2.
# End the game when a player wins three rounds using break and exit.
# Use continue to restart the round until one player wins three rounds.
# Your last bit of code should be the results of which player won.
# Create a counting system using a variable and += to keep track of the winner for each round.
# The while loop needs to be at the start of the game.
# Make sure you include print statements saying each player's final score at the end.
# Create an if statement to end the loop.
# You have created your first game involving scoring. Well done!

print("***ROCK PAPER SCISSORS GAME 2.0 "+"\U0001FAA8","\U0001F4C4"+"✂️","***")
print("Select your move (r, p, or s)")
print("Best of 3")
print()
# from getpass import getpass as input
rock ="r"
paper ="p"
scissors = "s"
player1WinCount = 0
player2WinCount = 0
while True:
  move1 = input("whats your move player 1? ")
  move2 = input("whats your move player 2? ")
  if move1 == move2:
    print("Player 1:",player1WinCount)
    print("Player 2:",player2WinCount)
    print("that round was a tie")
    if player1WinCount == 3:
      print("Player 1 Wins the game!")
      exit()
    elif player2WinCount == 3:
      print("Player 2 wins the game!")
      exit()
    continue
  elif move1 == rock and move2 == paper:
    print("player 1 wins that round!")
    player1WinCount +=1
    print("Player 1:",player1WinCount)
    print("Player 2:",player2WinCount)
    if player1WinCount == 3:
      print("Player 1 Wins the game!")
      exit()
    elif player2WinCount == 3:
      print("Player 2 wins the game!")
      exit()
    continue
  elif move2 == rock and move1 == paper:
    print("player 2 wins that round!")
    player2WinCount +=1
    print("Player 1:",player1WinCount)
    print("Player 2:",player2WinCount)
    if player1WinCount == 3:
      print("Player 1 Wins the game!")
      exit()
    elif player2WinCount == 3:
      print("Player 2 wins the game!")
      exit()
    continue
  elif move1 == scissors and move2 == rock:
    print("Player 2 wins that round!")
    player2WinCount +=1
    print("Player 1:",player1WinCount)
    print("Player 2:",player2WinCount)
    if player1WinCount == 3:
      print("Player 1 Wins the game!")
      exit()
    elif player2WinCount == 3:
      print("Player 2 wins the game!")
      exit()
    continue
  elif move2 == scissors and move1 == rock:
    print("Player 1 wins that round!")
    player1WinCount +=1
    print("Player 1:",player1WinCount)
    print("Player 2:",player2WinCount)
    if player1WinCount == 3:
      print("Player 1 Wins the game!")
      exit()
    elif player2WinCount == 3:
      print("Player 2 wins the game!")
      exit()
    continue
  elif move1 == scissors and move2 == paper:
    print("Player 1 wins that round!")
    player1WinCount +=1
    print("Player 1:",player1WinCount)
    print("Player 2:",player2WinCount)
    if player1WinCount == 3:
      print("Player 1 Wins the game!")
      exit()
    elif player2WinCount == 3:
      print("Player 2 wins the game!")
      exit()
    continue
  elif move2 == scissors and move1 == paper:
    print("Player 2 wins that round!")
    player2WinCount +=1
    print("Player 1:",player1WinCount)
    print("Player 2:",player2WinCount)
    if player1WinCount == 3:
      print("Player 1 Wins the game!")
      exit()
    elif player2WinCount == 3:
      print("Player 2 wins the game!")
      exit()
    continue

# REPLIT SOLUTION

# from getpass import getpass as input


# print("E P I C    🪨  📄 ✂️    B A T T L E ")
# print()
# print("Select your move (R, P or S)")
# print()
# #hint: create these variables outside loop and then add += with correct player to keep score throughout
# player1_score = 0
# player2_score = 0
# #hint: that the while loop needs to go around all code and then highlight the rest of the code and hit tab once. 
# while True: 
#   player1Move = input("Player 1 > ")
#   print()
#   player2Move = input("Player 2 > ")
#   print()
  
#   if(player1Move=="R"):
#     if(player2Move=="R"):
#       print("You both picked Rock, draw!")
#     elif(player2Move=="S"):
#       print("Player1 smashed Player2's Scissors into dust with their Rock!")
#       player1_score += 1
#     elif(player2Move=="P"):
#       print("Player1's Rock is smothered by Player2's Paper!")
#       player2_score += 1
#   elif(player1Move=="P"):
#     if(player2Move=="R"):
#       print("Player2's Rock is smothered by Player1's Paper!")
#       player1_score += 1
#     elif(player2Move=="S"):
#       print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
#       player2_score += 1
#     elif(player2Move=="P"):
#       print("Two bits of paper flap at each other. Dissapointing. Draw.")
#   elif(player1Move=="S"):
#     if(player2Move=="R"):
#       print("Player 2's Rock makes metal-dust out of Player1's Scissors")
#       player2_score += 1
#     elif(player2Move=="S"):
#       print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
#     elif(player2Move=="P"):
#       print("Player1's Scissors make confetti out of Player2's paper!")
#       player1_score += 1
  
# # hint: make sure you add player scores at the end of all the options but still inside the while loop.
#   print("Player 1 has", player1_score, "wins.")
#   print("Player 2 has", player2_score, "wins.")

#   if player1_score==3 or player2_score==3:
#     print("Thanks for playing!")
#     exit()
#   else:
#     continue
    