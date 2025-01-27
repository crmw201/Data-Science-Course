#5.1 Write Python code to take the name of a user's favourite restaurant and store in a a variable called string_fav
string_fav=input("Enter favourite restaurant: ")
#5.2 Below this, write a statement to take in the user's favourite number. Use casting to store it in an integervariable called int-fav
int_fav=int(input("Favourite number: "))
#5.3 Print out both these using two separate print statements below what you have written. Be careful!
print(string_fav)
print(int_fav)
#5.4 Once this is working, try to cast string_fav to an integer. What happens? Add a comment in your code to explain why this is.
int_string_fav=int(input("Enter favourite restaurant: "))
print(int_string_fav)
#It doesn't run. Is it because it recognises the input has no numbers in it so can't convert the letters into an integer.
