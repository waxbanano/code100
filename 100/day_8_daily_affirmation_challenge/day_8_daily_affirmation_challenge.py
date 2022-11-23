#Day 8 of 100 days of Python coding

# 👉 Day 8 Challenge
# Affirmations (or insults) Generator
# Today's focus is using all the skills you have learned so far:

# input and output
# concatenation
# if statements
# nested if statements
# Build a custom affirmations generator to give the user a customized affirmation each day of the week.

# Make sure you ask the user for their name, the current day of the week, and a few of their favorite things. All of this information should be used to help you build your affirmations.
# Think of these as variables.

# The goal is to generate a unique message for each day of the week based on the user's answers.
# use if and nested if statements

# Use concatenation to generate the affirmation.

# If affirmations are not your jam, then you could do a daily joke or insult. Please don't be mean. Keep it light and funny.

# Final challenge: Can you create if statements that do not care about capital or lowercase letters of names.

# Don't forget to restate the full question. name ==. The next chapter will explain this.
print("+++++DAILY AFFIRMATION REMINDER++++")
name = input("Whats your name? ")


if name == "Gandalf" or name == "gandalf" or name:
  print()
  print("Welcome Gandalf!")
  
  day = input("What day of the week is it? ")
  
  if day == "Sunday" or day == "sunday":
    print("Happy", day+"!","For the trouble is that we are self-centered, and no effort of the self can remove the self from the centre of its own endeavor.")

  elif day == "Monday" or day == "monday":
    print("Happy", day+"!","For the trouble is that we are self-centered, and no effort of the self can remove the self from the centre of its own endeavor. - William Temple")

  elif day == "Tuesday" or day == "tuesday":
    print("Happy", day+"!","The most important function of art and science is to awaken the cosmic religious feeling and keep it alive. - Albert Einstein")

  elif day == "Wednsday" or day == "wednsday":
    print("I always entertain great hopes. - Robert Frost")

  elif day == "Thursday" or day == "thursday":
    print("Happy", day+"!","You cannot devalue the body and value the soul - or value anything else. The isolation of the body sets it into direct conflict with everything else in creation. - Wendell Berry")

  elif day == "Friday" or day == "friday":
    print("Happy", day+"!","A wise man never loses anything if he have himself. - Montaigne")

  elif day == "Saturday" or day == "Saturday":
    print("Happy", day+"!","To wait for moments or places where no pain exists, no separation is felt and where all human restlessness has turned into inner peace is waiting for a dream world. - Henri J. M. Nouwen")
  else:
    print("error: I dont know that day? I Hope you are feeling better soon!")
else:
  print()
  print("***************   YOU ARE NOT KNOWN!   ***************")
  print()
  print("Many that live deserve death. Some that die deserve life.")
  print()

#REPLIT SOLUTION


# print("Hello. Welcome to your daily affirmation generator.")
# name = input("What is your name?")



# if name =="Mark" or name == "mark":
#  DOW = input("What is the day of the week?")
#  if DOW == "monday" or DOW == "Monday":
#    print("It is going to be a great Monday", name)
#  if DOW == "tuesday" or DOW == "Tuesday":
#    print("What a wonderful Tuesday it is", name)
#  if DOW == "wednesday" or DOW == "Wednesday":
#    print("Happy Hump Day", name)
#  if DOW == "thursday" or DOW == "Thursday":
#    print(name,"your week is almost over!")
#  if DOW == "friday" or DOW == "Friday":
#    print(name, "It's FRIDAY!")

# elif name == "David" or name== "david":
#  DOW = input("What is the day of the week?")
#  if DOW == "monday" or DOW == "Monday":
#    print("It is going to be a great Monday", name)
#  if DOW == "tuesday" or DOW == "Tuesday":
#    print("You look great in that color", name)
#  if DOW == "wednesday" or DOW == "Wednesday":
#    print("You look chipper today", name)
#  if DOW == "thursday" or DOW == "Thursday":
#    print(name,"you are doing a great job!")
#  if DOW == "friday" or DOW == "Friday":
#    print(name, "it's FRIDAY!")
# else:
#  print("I do not know your name, but I hope you are having a great day!")

#EXTRA EXTRA

# print("Wholesome Positivity Machine")
# print("\n")
# name = input("Who are you?" )
# achieve = input("What do you want to achieve? ")
# feel = input("On a scale of 1-10 how do you feel today? (1 = worst, 10 = best ")

# if feel == "1":
#   print("Hang in there",name+"!!","Today you're going to",achieve,"simply by being you - YOU ROCK")
# elif feel == "2":
#   print("Hang in there",name+"!!","Today you're going to",achieve,"simply by being you - YOU ROCK")
# elif feel == "3":
#   print("You are doing great",name+"!!","Today you're going to",achieve,"simply by being you - YOU ROCK") 
# elif feel == "4":
#   print("Life happens",name+"!!","Today you're going to",achieve,"simply by being you - YOU ROCK")
# elif feel == "5":
#   print("Things are good",name+"!!","Today you're going to",achieve,"simply by being you - YOU ROCK")
# elif feel == "6":
#   print("",name+"!!","Today you're going to",achieve,"simply by being you - YOU ROCK")
# elif feel == "7":
#   print("Hang in there",name+"!!","Today you're going to",achieve,"simply by being you - YOU ROCK")
# elif feel == "8":
#   print("Hang in there",name+"!!","Today you're going to",achieve,"simply by being you - YOU ROCK")
# elif feel == "9":
#   print("Excellent work",name+"!!","Today you're going to",achieve,"simply by being you - YOU ROCK")
# elif feel == "10":
#   print("LETS GO",name+"!!!","Today you're going to",achieve,"simply by being you - YOU ROCK")

# else:
#   print("hmmm")

