#Day 6 of 100 days of Python coding

# What the elif is this?
# The elif command (which stands for 'elseif') allows you to ask 2, 3, 4 or 142 questions using the same input! This command must be in a certain place. You can have as many elif statements as you want, but they must go in between if and else and have the same indentation. The print statements in your elif command need to line up with the indent of the other print statements.
 

# Where would an elif statement go in the code below?

# print("SECURE LOGIN")
# username = input("Username > ")
# if username == "mark":
#   print("Welcome Mark!")
#   #HERE
# else:
#   print("Go away!")

# An elif statement would go in between the if and else statements.


# 👉 Add this elif statement to the code above. Make sure you indent properly AND put it in between the if and else statements!

# elif username == "suzanne":
#   print("Hey there Suzanne!")
 

# Your code should look like this:

# print("SECURE LOGIN")
# username = input("Username > ")

# if username == "mark":
#   print("Welcome Mark!")
# elif username == "suzanne":
#   print("Hey there Suzanne!")
# else:
#   print("Go away!")
# How easy was that? You will be a pro in no time!

# print("SECURE LOGIN")
# username = input("Username > ")
# password = input("Password > ")
# if username == "Gandalf" and password == "bestWizard":
#   print("Welcome Gandalf!")
# elif username == "Bilbo" and password == "shire1":
#   print("Hey there Bilbo!")
# elif username == "Frodo" and password == "ilovebilbo":
#   print("Greetings Frodo")
# else:
#   print("You shall not pass!")

# Common Errors
# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# Syntax Error
# 👉 What is wrong the code below?

# print("SECURE LOGIN")
# username = input("Username > ")

# if username == "mark":
#   print("Welcome Mark!")
# else:
#   print("Go away!")
# elif username == "suzanne":
#   print("Hey there Suzanne!")
# The elif statement is in the wrong place. It must go in between the if and else statements.

# print("SECURE LOGIN")
# username = input("Username > ")

# if username == "mark":
#   print("Welcome Mark!")
# elif username == "suzanne":
#   print("Hey there Suzanne!")
# else:
#   print("Go away!")

# season = input("what is your favorite season?")
# if season == "spring":
#   print("Ah! The birds are chirping and flowers blooming.")
# elif season == "summer":
#   print("Catch some sun and cool off with a lemonade.")
# elif season == "autumn":
#   print("The leaves are changing and the air is crisp. Enjoy!")
# elif season == "winter":
#       print("Stay warm by the fire and watch the snow fall.")
# else: 
#   print("I don't know that season. Please try again.")

# 👉 Day 6 Challenge
# Make your own login program.
# 1. Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting.
# 2. Write a specific personalized greeting for 3 different people.
# 3. Don't forget an else statement for everyone else who shouldn't be logging in.
print("MY LOGIN SYSTEM")
print("++++++++++++++++")
username = input("Username -> ")
password = input("Password -> ")
print()
if username == "Rick" and password == "morty":
  print("Come on, Morty. Just take it easy, Morty. It's gonna be good. Right now, we're gonna go pick up your little friend Jessica.Morty! You-you don't have to worry about me getting with Jessica or anything. Sh-sh-she— she, she, she's all for you, Morty.")
elif username == "Morty" and password == "ilovejessica":
  print("I'm taking charge of this situation, buddy! I'm put—I’m, I'm, I'm, I'm puttin’... I-I’m, I’m, I’m not gonna stand around like some sort of dumb... dumb person and just le-let you ruin the whole world!")
elif username == "Summer" and password == "frankisgod":
  print("Oh my God, his head is in his food. I'm going to puke. maybe you were out all night again with Grandpa Rick. Oh my god, my parents are so loud, I want to die.")
elif username == "MrPoopyButthole" and password == "oohwee":
  print("OOH WEE!!")
else:
  print("Credentials Can NOT be Verified, Please dont try again!")


#REPLIT SOLUTION
# print("Secure Login")
# username = input("What is your username?")
# password = input("What is your password?")

# if username == "David" and password == "PyTh0nR*cks":
#   print("Welcome, David! You are looking nice today!")
# elif username == "Becky" and password == "Repl!t4evEr":
#   print("Hi Becky! Love your hair today!")
# elif username == "Bill" and password == "SmashTHEb*gs!":
#   print("Yo! Bill! What up?!")
# else:
#   print("You do not have access. Go away!")