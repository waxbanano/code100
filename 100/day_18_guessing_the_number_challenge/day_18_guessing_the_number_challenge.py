# Day 18 of 100 days of coding

# 👉 Day 18 Challenge
# We are going to build a "Guess the Number" guessing game.

# You are going to use a while loop and some of the concepts from the past few days.

# Start by picking a number between 0 and 1,000,000. This will be your first variable.
# Essentially, what do you want the correct number to be. Create a variable for that number.
# Create a while loop to keep asking the user to guess your number.

# If they are too low, tell them "too low." If they guess too high tell, them "too high."

# You will need to include if statements here with logical operators. Include the correct number variable you created at the beginning in these if statements.

# If the user guesses correctly, tell them they are a winner (maybe add a fun emoji too!)
# If they are a winner, they need to get out of the loop. How do you do that?

# Count the number of attempts it took for the user to guess number. Make sure you only show that after they get the answer correct.
# Create a counter before the while loop and print the number of attempts after the user is a winner. Don't forget to count attempts using += in the loop.

# Extra challenge: If the user types a negative number, exit program.

print("+++ GUESS THE NUMBER! v1.0 +++")
print("Can you guess what number i'm thinking of?")
setTheNumber = 69420
tries = 1
while True:
  guess = int(input("Guess a number between 1 and 1000000 -->"))
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
    tries +=1
    continue
  elif guess > setTheNumber:
    print("Thats not the number i was thinking of, try a lower number.")
    tries +=1
    continue

#REPLIT ANSWER
# print("Welcome to Guess the Number.")
# print()
# print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low, too high, or get it correct.")
# print()
# print("Let's play!")

# correct_number = 2300
# attempt = 1

# while True:
#   user_guess = int(input("Pick a number between 1 and 1,000,000: "))
#   if user_guess < 0:
#     print("Now we'll never know what the answer is …")
#     exit()
#   if user_guess < correct_number:
#     print("That number is too low. Try again!")
#     attempt += 1
#   elif user_guess > correct_number:
#     print("That number is too high. Try again!")
#     attempt += 1
#     continue
#   elif user_guess == correct_number:
#     print("You are a winner! 🥳🥳")
#     break 
#   else:
#     print("That is not a number I recognize.")
# print("It took you", attempt, "attempt(s) to get the correct answer.")    
  


    
  
  
  