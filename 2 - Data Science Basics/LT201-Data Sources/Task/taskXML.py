import xml.etree.ElementTree as ET

tree = ET.parse('movie.xml')
root = tree.getroot()

# USe the iter() function to list all the child tags of the movie element
# which should be; format, year, rating, description if I understand it 
# correctly
# for xxxx in root.iter('xxxx'):
    #print

for movie in root.iter('movie'):
    print(f"Movie Title: {movie.get('title')}")
    for child in movie:
        print(f"{child.tag}, {child.text}")
    print("-" * 50)

# use the itertext function to print out the movie descriptions
# NB make sure to concatenate the text and strip white spaces before print

for movie in root.iter('movie'):
    print(f"Movie Title: {movie.get('title')}")
    for child in movie:
        if child.tag == 'description':
            description_text = ''.join(child.itertext()).strip()
            print(f"Description: {description_text}")
    print("-" * 50)

# Find the number of movies that are favourites and the number of movies
# that are not
# Use counters and if 'True'

favourite = 0
not_favourite = 0

for movie in root.iter('movie'):
    if movie.get('favorite') == "True": # Beware of American vs. British spellings of 'favourite' !!
        favourite += 1
    else:
        not_favourite += 1

print(f"Favourite Movies Counted: {favourite} ")
print(f"Not Favourite Movies Counted: {not_favourite} ")

