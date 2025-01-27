#2.1 Ask the user to enter a sentence using the input() method.
#Save the user's response in a variable called str_manip

str_manip=input("Enter sentence: ")

#2.2 Calculate and display the length of str_manip
#Calculate the length of str_manip and save as variable length
#Print length 

length=len(str_manip)
print(length)

#2.3 Find the last letter in str_manip
#Save as variable last_letter
#Print last_letter
#2.4 Replace every occurence of this last letter with '@'
#Replace occureences of last letter using replace function
#print  
#NB: This works when I use "s" but doesn't work when
#I use "last letter" in the replace bracket. If the sentence input is changing depending on what the 
#user enters wouldn't it make more sense to use a variable there?

last_letter=str_manip[-1: ]
print(last_letter)

replaced_str_manip=str_manip.replace("s", "@")
print(replaced_str_manip)   

#2.5 Print the last 3 characters in str_manip backwards
#Identify the last 3 letters and save as variable end_three
#print end_three
#Reverse them
#Print 

end_three=str_manip[-3:]
print(end_three)
reverse_end_three=end_three[ : :-1]
print(reverse_end_three)

#2.6 Create a five letter word that is made up of the first 3 characters
#and the last two characters in str_manip
#Use slicing to identify beginning 3 letters (first_three)
#Identify last two letters (last_two)
#Add strings together
#Print combined strings

first_three=str_manip[0:3]
last_two=str_manip[-2:]
five=first_three+last_two
print(five)
