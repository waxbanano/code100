# Day 13 of 100 days of Python coding
# 👉 Day 13 Challenge
# Grade Generator
# This project is going to take some time (and some hard thinking) but will be brilliant once you have it working!

# You are going to ask the user to type in the name of a test, maximum score they could receive, and how many points they received. For example, your test could be called "Python Skills" and the maximum score is 50 points and the user receives 30 points out of 50 possible points.
# What do you need to add to your input when using whole numbers?

# 2. Figure out the percentage the user received and round to 2 decimal places.
# You will need to divide to determine the total score the user received. Don't forget to round.

# Use if/elif statements to show users the letter grade they received.
# Think about the symbols: <, >, etc. Don't forget to restate the full question with the variable name (like you did on day 8).

# At the end, the user should see the letter grade they received and the percentage correct.

# Add in emojis to celebrate their good grade or different colors depending on what you think is a good or bad final grade.

 

# Here is a grading scale to help you decide the letter grade the user received (feel free to use a different grading scale if you like.)

# Letter Grade	Percentage
# A+	90-100
# A	80-89
# B	70-79
# C	60-69
# D	50-59
# U	under 50

print("+++Grade Generator+++")
testName = input("Whats the name of the test? ")
questions = int(input("How many questions was the test? "))
questionsCorrect = int(input("How many questions were answered correctly? "))
print("Test name:", testName)
print("total questions:", questions)
print("questions answered correctly:", questionsCorrect)
decimalScore = questionsCorrect/questions
roundDecimalScore = round(decimalScore, 2)
score = int(roundDecimalScore*100)
print("score:", score,"% percent")

if score == 100:
  print(score,"% percent is an A+")
elif score >= 90 or score <= 99:
  print(score, "% percent is an A")
elif score >= 80 or score <= 89:
  print(score,"% percent is a B")
elif score >= 70 or score <= 79:
  print(score,"% percent is a C")
elif score >= 60 or score <= 69:
  print(score, "% percent is a D")
else:
  print(score,"% percent is an F")


# print("Exam Grade Calculator")
# print()
# name_of_exam = input("Name of exam: ")
# print()
# total_score = int(input("Max. Possible Score:"))
# your_score = int(input("Your score: "))
# print()



# number_score = float(your_score / total_score)
# final_number = round(number_score, 2)
# final_perc = round(float(your_score / total_score)*100, 2)

# print("You got",final_perc,"%")

# if final_number >= .90:
#   print("Your letter score is an A+")
# elif final_number >= .80 and final_number <= .89:
#   print("Your letter grade is an A-.")
# elif final_number >= .70 and final_number <= .79:
#   print("Your letter score is a B.")
# elif final_number >= .60 and final_number <= .69:
#   print("Your letter grade is a C.")
# elif final_number >= .50 and final_number <= .59:
#   print("Your letter grade is a D.")
# elif final_number <= .49:
#   print("Your letter grade is a U.")
# else: 
#   print("Try again!")