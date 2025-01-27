#Ask the user to input their full name

full_name=input("Enter full name: ")

#Perform some validation to check that the user has entered a full name
#Use a len() function to calculate the number of characters entered and save as variable num_characters
#We can then use the if function to say if num_characters==0
#print "You haven't entered anything"
#Then we can use the elif fucntion to say if num_characters < 4
#Print "You have entered less than 4 characters. Please make sure that you have entered your name and surname"
#Same again elif but if num_characters > 25 
#Print "You have entered more than 25 characters. Please make sure that you have only entered your full name."
#Else 
#Print "Thank you for entering your name."

num_characters=int(len(full_name))

if num_characters==0:
    print("You haven't entered anything.")
elif num_characters < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
elif num_characters > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name")
else: 
    print("Thank you for entering your name")
