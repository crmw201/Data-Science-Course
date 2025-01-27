
# Get the user input of desired location with a bit of a story

print("Welcome to Holidays4u. You have won a discounted trip to one four" +
" select locations: Senegal, Corfu, Wales or Peru!")

city_flight = input("Please enter which of these destinations you wish" +
" to travel: ")

# Get the number of nights and rental car days

num_nights = int(input("How many nights do you wish to book for?: "))
rental_days = int(input("How many days do you wish to rent a car for?: "))

print("Great, Thanks!")

# Create the four functions required, first hotel cost

def hotel_cost (num_nights):
    hotel_price_per_night = 50
    return hotel_price_per_night * num_nights

# Question: If had more time would it not make sense to set out a dictionary
# and try and get assigned prices per night of hotels in each region and 
# work that into the fucntion, as well as a dictionary for the plane 
# costs rather than if- elif - else ? If so would like to see how that 
# could be done as imagine it would get quite fiddly!

# Function for plane cost using if-elif-else

def plane_cost (city_flight):
    if city_flight.lower() == "senegal":
        return 450
    elif city_flight.lower() == "corfu":
        return 350
    elif city_flight.lower() == "wales":
        return 150
    elif city_flight.lower() == "peru":
        return 750
    else:
        return 0

# Function for calculating car rental cost

def car_rental (rental_days):
    daily_car_rental_cost = 25
    return daily_car_rental_cost * rental_days

# Function to calculate total holiday cost with 3 arguments

def  holiday_cost(num_nights, city_flight, rental_days):
  return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

print("Total cost: ", holiday_cost(num_nights, city_flight, rental_days))

# Have made the suggested changes, but what threw me off is in the question 
# it asks for hotel_cost, plane_cost and car_rental to be the arguments so I
# still don't quite get that

