# Ask the User Variables

destination = input("what is your destination? ")
distance = float(input("how many miles? "))
car_fuel = float(input("what is the car's fuel in miles per gallon? "))
gas_price = float(input("what is the price per gallon? "))
nights = int(input("how many nights will you stay? "))
hotel = float(input("what is the hotel cost per night? "))
food = float(input("what is the daily food budget? "))

# Calculate the variables here

gallons_needed = distance / car_fuel
total_gas_cost = car_fuel * gas_price
total_hotel_cost = nights * hotel
total_food_cost = (nights +1) * food
grand_total = total_gas_cost + total_hotel_cost + total_food_cost


# Project starts here

print(f"\n=== Road Trip Budget Planner ===\n") 

print(f"Destination: {destination}")
print(f"Distance: {distance}\n")

print(f"--- Cost Breakdown ---")
print(f"Gas ({car_fuel} gal @ ${gas_price:.2f}/gal):   ${total_gas_cost:.2f}")
print (f"Hotel ({nights} nights @ ${hotel:.2f}):    ${total_hotel_cost:.2f}")
print(f"Food ({(nights +1)} days @ ${food:.2f}):        ${total_food_cost:.2f}")
print("-" * 40)
print(f"Estimated Total:               ${grand_total:.2f}")