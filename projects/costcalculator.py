# Create a Python script that asks a user questions in the command line. 
# The script should follow the outlined specifications.

# Specifications:
# Receive the following arguments from the user:
    # Kilometers to drive
    # Liters-per-kilometer usage of the car
    # Price per liter of fuel
# Calculate the cost of the trip and display it to the user in the console. 
# Apply some of the string formatting tricks that you learned about in this course section.

distance = float(input("how many kilometers do you want to drive? "))
fuel_Usage = float(input("How much liters per kilometer does your car use? "))
liter_price = float(input("how much does a liter of fuel cost? "))
trip_price = (distance * fuel_Usage) * liter_price

print(f"total cost of your trip is:{trip_price:^10}")