#3.1 Ask the user to enter three different integers
#Using input function on 3 different lines request 3 integers

integer_one=int(input("Enter number: "))
integer_two=int(input("Enter number: "))
integer_three=int(input("Enter number: "))

#3.2 Print out the sum of all the numbers
# Calculate sum of three numbers
# print sum_of_three

sum_of_three=integer_one + integer_two + integer_three
print(sum_of_three)

#3.3 The first number minus the second number
# Calculate first minus second (first_minus_second)
# Print first_minus_second

first_minus_second=integer_one-integer_two
print(first_minus_second)

#3.4 Multiply the third number by the first number
#Calculate third number times first number (third_times_first)
#Print third_times_first

third_times_first=integer_one * integer_three
print(third_times_first)

#3.5 Summ all three numbers and divide by the third number
#Use sum_of_three variable calculated above
#Calculate sum divided by third number (sum_div_three)
#Print sum_div_three

sum_div_three=sum_of_three/integer_three
print(sum_div_three)
