#Save "The!quick!brown!fox!jumps!over!the!lazy!dog! as a string 
# Use replace() function to replace every "!" with a blank space
# Print spaced_sentence
# Use upper() function to chage all letters to upper case, while maintaining spaces
# Print upper_sentence
# Reverse sentence using slicing
# Print reverse_sentence

sentence="The!quick!brown!fox!jumps!over!the!lazy!dog!"
spaced_sentence=sentence.replace("!", " ")
print(spaced_sentence)
upper_sentence=spaced_sentence.upper()
print(upper_sentence)
reverse_sentence=(upper_sentence[::-1])
print(reverse_sentence)
