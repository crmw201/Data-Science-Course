# Make a string with every other character an upper case
# (help from LT109 Lecture video)

sentence = "I am learning to code"
alternating_letter_sentence = ""  # This is going to store the updated string

for i in range(len(sentence)): 
    if i % 2 == 0: 
        alternating_letter_sentence += sentence[i].upper()

    else:
        alternating_letter_sentence += sentence[i].lower()

print(alternating_letter_sentence)

# ************** Part 2 ***************
# Using the same string make each alternative word lower and upper case

final_sentence = ""

#Split string into words
split_sentence = sentence.split() 
#Now have 5 words to iterate through

#Iterate same as above
for i in range(len(split_sentence)):
    if i % 2 == 1:
        final_sentence += split_sentence[i].upper()
    else:
        final_sentence += split_sentence[i].lower()

#Need to join all back together with spaces
joined_string = "".join(final_sentence)

print(final_sentence)

# Can't work out how or why to get the spaces between the words and not 
# the letters without having to index this phrase and start another for loop
