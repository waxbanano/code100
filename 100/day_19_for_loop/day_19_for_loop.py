#Day 19 of 100 days of code

# For Loop
# A while loop is perfect to use when we don't know how many times we want the loop to repeat.

# If we have an idea of how many times we want the loop to repeat, we can use a for loop to loop code in exactly the same way the while loop did.

# However, we can set up the variable, control condition, and increment all in ONE line of code.



# Let's compare
# Here is how we created a counter with a while loop:

# counter = 0
# while counter < 10:
#   print(counter)
#   counter += 1
# And here is the same counter using a for loop:

# for counter in range(10):
#   print(counter)

# Range
# The range function creates a list of numbers in the range you create. If you only give it one number, it will start at 0 and move to a state where the final number is one less than the number in the brackets. In this case, the final number would be 9.

# range(10)
# Note: The variable is only there during the loop, not after it is completed.

# Commonly computer programmers use the variable names i, j, and k when using for loops for counter. There is no real reason. It's just how everyone has always done it. However, feel free to use a variable that has a bit more meaning if you like.

# Common Errors
# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# Invalid Syntax
# 👉 This program will add all the numbers from 0 to 99 and continually print out the total. Why is it not working?

# total = 0
# for number in range 100:
#   total += number
#   print(total)
# We forgot the () with the range. The brackets are important because range is a function (like the exit function). What range is doing is creating a list of numbers between 0 and the number we put in the brackets. If there are no (), it won't work.

# for number in range (100):
# Name Error
# 👉 In this program, the computer should be printing out day + numbers 1-6. Why is it saying 'day is not defined'?

# for days in range(7):
#   print("Day", day)
# The variable name is wrong inside the code. If you want to refer to a created variable in a for loop, you have to spell it the same way each time.

#   print("Day", days)
# Fix My Code
# 👉 Try and fix this code which is full of errors.

# First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

# total = 10
# while counter in range 100:
#   total += 10
#   print("total")
  
# total = 10
# for total in range(100):
#   total += 10
#   print(total)

# 👉 Day 19 Challenge
# A common thing people do is borrow money. When people repay money, they pay interest which is paid back annually and added to the original amount the person borrowed.

# You are going to create a loan calculator that shows how much money you owe for a loan of $1,000 with a 5% APR (APR is fancy for Annual Percentage Rate) over 10 years.

# This means each year the amount of money you owe will increase 5%.

# Figure out how much you owe altogether for 10 years?

# Use a for loop and one or two lines of looped code to determine the answer. (Hint: Don't make this overcomplicated. It should only be a few lines of code altogether.)

# Make sure the for loop happens 10 times.
# Start your value (amount you are borrowing) before the loop starts.
# If you need to count on one more number, just write i+ in the print statement to tell the computer to add the next number.

loan = 1000
for number in range(10):
  loanInterest = loan * .05
  loan += loanInterest
  print("loan interest for year",number+1,"is",round(loanInterest,2))
  print("loan total for year",number+1,"is",round(loan,2))
  print()
  
