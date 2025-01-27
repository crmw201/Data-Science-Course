# Write a program that always asks the user to enter a number.


total = 1 # Create a variable that will hold value of all user inputs.
entries = -1 # Varibale to count entries

# When the user enters -1, the program should stop requesting the user
# to enter a number. (received help from lecture vid)

user_input = 0

#if user_input == 0 :
    #print("No values were entered")

while user_input != -1:
    
    user_input = int(input("Please enter a number (-1 to exit): "))
    total += user_input 
    entries += 1                #(entries = entries + 1)
    if user_input == 0:
        print("You have entered a zero value")
        continue
    elif user_input == "":
        print("You have entered no value")
        continue
    elif user_input == -1:
        break

# The program must then calculate the average of the numbers entered, 
# excluding the -1

print(total)
print(entries)
average = total / entries
print(average)


