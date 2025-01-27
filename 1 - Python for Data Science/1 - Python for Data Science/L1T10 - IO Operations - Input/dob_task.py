
file = open('DOB.txt', 'r+')
all_info = file.readlines()        

#readlines put all the data into list form, (strip removes /n character)

# print(all_info)

# Thinking being to index each line 1-5, then print under 'Name'
# indices 1 + 2 , then do the same 3,4,5.

print("Name")
for line in all_info:
    line = line.strip() #To remove the spaces 
    line = line.split()
    name = line[:2]
    print(" ".join(name))

print()

print("Birthdate")
for line in all_info:
    line = line.strip() 
    line = line.split()
    birthdate = line[2:]
    print(" ".join(birthdate))


file.close()

