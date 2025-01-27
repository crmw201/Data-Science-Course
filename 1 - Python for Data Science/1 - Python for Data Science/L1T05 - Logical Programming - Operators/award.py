"""
5. Design a program that determines the award a person competing in 
a triathlon will receive. Program should read the time in minutes for
all three events and then calculate and display the total time taken
to complete the triathlon. The award is based on total time taken. 
The qualifying time for awards is 100 minutes. Display the award the 
participant will recieve based on the criteria:
0-100: Provincial Colours
101-105: Provincial Half Colours
106-110: Provincial Scroll
111+ : No award

It says in the question qualifying time for awards is 100 minutes.
But doesn't less than 100 mins qualify as Provincial Colours?

"""

#Get the event inputs
swim_time=int(input("Enter swim time in minutes: "))
cycle_time=int(input("Enter cycle time in minutes: "))
run_time=int(input("Enter run time in minutes: "))

#Sum the three inputs to get total time
total_time= swim_time + cycle_time + run_time

#Display total time taken 
print(total_time)

#Assign award participant should receive
if (total_time < 100):
    print("Provincial Colours")
elif (total_time > 100) and (total_time <= 105):
    print("Provincial Half Colours")
elif (total_time > 105) and (total_time <= 110):
    print("Provincial Scroll")
else:
    print("No award")
