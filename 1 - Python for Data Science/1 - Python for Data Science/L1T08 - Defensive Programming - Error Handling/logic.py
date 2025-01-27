# Example of code with a logical error. 

# This program is designed to identify if a user is eligible to ride on 
# a rollercoaster depending on their height input. Anyone taller than
# or equal to 220cm, or shorter than 100cm will be ineligible.

height = int(input("What is your height in centimetres?: "))
if height > 220:
    print ("You are too tall for this ride")
elif height < 100:
    print ("You are too short for this ride")
else:
    print ("Enjoy the ride!")

# Program runs but logical error lies in when entering 220, output is 
# still "Enjoy the ride". To fix this it should be height >= 220.