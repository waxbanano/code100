# Day 11 of 100 days of Python coding
# 👉 Day 11 Challenge
# How many seconds are in a year?
# Use the power of breaking a program down into its parts. We could Google this, but why not make a program for this instead.

print("++ seconds in a year calculator ++")

# 1 minute = 60 seconds
minute = int(60) 
# 60 minutes = 1 hour
hour = int(60*minute)
# 24 hours = 1 day
day = int(24*hour)
# 31 days = 1 month
month = int(31*day)
# 12 months = 1 year
# year = int(12*month)
# 365 days = 1 year
year = int(365*day)
leapYear = int(366*day)
howMany = int(input("How many days are in the year to be calculated? "))
if howMany == 365:
  print(year,"seconds in a year")
elif howMany == 366:
  print(leapYear,"seconds in a leap year")
else:
  print("that doesn't seem right.")


# 366 day = 1 leap year (this is every four years)

# Learn more about leap years here.

# You can multiply a bunch of numbers to figure out how many seconds are in a year.
# Think about how the math would be different for a leap year.
# Use input and if statements to add the extra day for leap year.
# Think about if you need int or float for your input.

# Make the computer do all the hard work and math for you. You do the thinking beforehand.