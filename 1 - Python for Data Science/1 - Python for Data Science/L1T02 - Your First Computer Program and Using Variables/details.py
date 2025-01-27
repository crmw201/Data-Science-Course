
#Pseudo Code for Task 2.1
#Request user's name
#Store input into variable called 'user_name'
#Request user's age
#Store input into variable callled 'user_age'
#Request user's House number
#Store input into variable callled 'house_number'
#Request user's street name
#Store onput into variable called 'street_name'
user_name=input("Enter your name:")
user_age=int(input("Enter your age:"))
house_number=int(input("Enter your house number:"))
street_name=input("Enter your street name:")
#Pseudo code for 2.1
#Print "name", "age", "house_number", "street_name" (due to requirement of task it is ok in this instance to have them all as strings? not say age=int(input("Enter your age:"))
print("This is {}.".format(user_name)+ " He is {} years old".format(user_age)+ " and lives at house number {}".format(house_number)+ " on {}.".format(street_name))
#I found online between phrases you have to put a '+', which is not in the material