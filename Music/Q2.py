# Define a class Scooter with the required attributes and methods as specified in the prompt.
class Scooter:
    def __init__(self, rental_company, starting_fee, price_per_100_meters, available_distance):
        self.rental_company = rental_company
        self.starting_fee = starting_fee
        self.price_per_100_meters = price_per_100_meters
        self.available_distance = available_distance

# Define the method price, which takes the length of the ride in kilometers as an argument. 
#  However, if the ride length exceeds the scooter's available 
# riding distance, the method returns the integer 1000.

    def price(self, length):
        # If the ride length requested does not exceed the available riding distance of the scooter, 
        # the method returns the price of a ride of that length, taking into account the starting fee 
        # and the price per 100 meters.
        if length <= self.available_distance:
            return round(self.starting_fee + length * self.price_per_100_meters * 10, 2)
        else:
            return 1000

    # Define the method ride, which takes the length of the ride as an argument and subtracts 
    # it from the available riding distance.
    def ride(self, length):

        # If the available riding distance becomes exhausted, it assigns the value 0 to the distance field.
        if length <= self.available_distance:
            self.available_distance -= length
        else:
            self.available_distance = 0

    # Define a method charge, whose argument is the number of kilometers, and which increases the 
    # available riding distance of the scooter by the given number of kilometers.
    def charge(self, distance):
        self.available_distance += distance

# Define a class Rental that takes a list of Scooter objects as input.
class Rental:
    def __init__(self, scooters):
        self.scooters = scooters

    # Implement the display_choices method in the Rental class that takes the length of the 
    # ride in kilometers as an argument, and prints the name of each scooter and the price of the 
    # ride, ordering the scooters from top to bottom, starting with the cheapest. 
    def display_choices(self, length):

        # To find the price of the ride, i called the price method of the Scooter class.
        prices = {scooter.rental_company: scooter.price(length) for scooter in self.scooters}
        sorted_prices = sorted(prices.items(), key=lambda x: x[1])
        for scooter_name, price in sorted_prices:
            print(f"{scooter_name}: {price}")

    # Implement the rent method in the Rental class that takes the name of the scooter the user 
    # wants to ride and the length of the ride.
    def rent(self, scooter_name, length):
        scooter = next((scooter for scooter in self.scooters if scooter.rental_company == scooter_name), None)        
        
        #If there is no scooter print the error message
        if scooter is None:
            print("Scooter not found")

        #Else if the requested length of the scooter is less than the length, print the error message
        elif scooter.available_distance < length:
            print("Not enough available distance for the ride")
        
        #Else print the rented scooter, the lenght and the the cost
        else:
            price = scooter.price(length)
            scooter.ride(length)
            print(f"You rented {scooter_name} for {length} km at a cost of {price}")

    # Implement the charge_scooter method in the Rental class that takes the name of the scooter 
    # to be charged and the number of kilometers as arguments. 
    def charge_scooter(self, scooter_name, distance):
        scooter = next((scooter for scooter in self.scooters if scooter.rental_company == scooter_name), None)
        
        #If there is no scooter print the error message
        if scooter is None:
            print("Scooter not found")

        # Else this method increases the available riding distance of the scooter by the 
        # requested number of kilometers (using the charge method of the Scooter class)
        else:
            scooter.charge(distance)
            print(f"{distance} km added to {scooter_name}'s available distance. Total available distance: {scooter.available_distance} km")


# In the main program, prompt the user to enter the details of three scooters: 
# Bolt, Tuul, and Bird, with their respective attributes and split the values with a comma ",".
scooters = []
for i in range(3):
    rental_company, starting_fee, price_per_100_meters, available_distance = input("Enter rental company, starting fee, price per 100 meters, and available distance (separated by commas): ").split(",")
    starting_fee = float(starting_fee)
    price_per_100_meters = float(price_per_100_meters)
    available_distance = float(available_distance)
    scooter = Scooter(rental_company, starting_fee, price_per_100_meters, available_distance)

    # Create instances of the Scooter class for each of the three scooters using the input data.
    scooters.append(scooter)

# Create an instance of the Rental class and pass a list of the three scooter objects to it.
rental = Rental(scooters)

# Call the display_choices method of the Rental class with an argument of 2.
rental.display_choices(2)

# Call the rent method of the Rental class for each of the three scooters, 
# with appropriate arguments, as specified in the prompt.
rental.rent("Bolt", 3)

rental.rent("Tuul", 18)

rental.rent("Tuul", 5)

# Call the charge_scooter method of the Rental class for the Tuul scooter, 
# with appropriate arguments, as specified in the prompt.
rental.charge_scooter("Tuul", 5)

# Call the rent method of the Rental class again for the Tuul scooter, 
# with appropriate arguments, as specified in the prompt.
rental.rent("Tuul", 2)