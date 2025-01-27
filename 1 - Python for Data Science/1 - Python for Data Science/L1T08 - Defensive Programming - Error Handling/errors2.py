# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Syntax Error - Missing "" to  indicate string
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth" # Logical Error - Add f to make it an f string

print(full_spec) # Syntax Error - Missing parentheses 