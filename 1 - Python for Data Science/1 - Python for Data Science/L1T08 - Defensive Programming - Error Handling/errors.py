# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the 
# error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax error - No use of parentheses
print ("\n") # Syntax Error - Indentation error and again no use of parentheses

# Variables declaring the user's age, casting the str to an int, 
# and printing the result
# Runtime Error - No need to have age_str as a string, and try to 
# convert, just have age=24, and convert str(age)  in print statement

age = 24 # Syntax error - Indentation error
print("I'm " + str(age) + " years old.") # Syntax Error - Indentation 
# error & spacing error 


# Variables declaring additional years and printing the total years of age
years_from_now = "3" # Syntax Error - Indentation error
total_years = age + int(years_from_now) # Syntax Error & Runtime Error 
#- 1. Indentation Error 2. Convert years_from_now to an integer

print ("The total number of years:" + str(total_years)) 

# Syntax Error & Runtime Error - 1. No use of parentheses 2. No variable called 
# 'answer_years', amend to 'total_years' 3. Convert total_years to a str

# Variable to calculate the total amount of months from the total amount
# of years and printing the result

total_months = total_years * 12 
# Runtime Error - No variable 'total', amend to 'total_years'
months_this_year = 6
print ("In 3 years and 6 months, I'll be " + 
       str(total_months+ months_this_year) + " months old") 
# Syntax Error & Runtime error - No parentheses 2. Convert total_months to str

#HINT, 330 months is the correct answer
# Answer was coming out as 324 months old, so needed to account for the
# 6 months, by adding variable months_this_year