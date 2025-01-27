# Use an if-else statement in combination with a single for loop to 
# create the star pattern shown in the question

#How do we get the descending scetion? Need 6th line (i=6), to equate to
# 4. x= i + 4, where i=6, so x=10. So for output x, x = 10 -i. So we can
# then run numbers * (10-i) for i>5.

numbers = "*" #Used this to avoid too many "*" to avoid contfusion in 
#workings out

for i in range (1, 10) :
    if i<=5 :
        print(i * numbers)
    else:
        print(numbers * (10-i))
    
