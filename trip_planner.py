# trip_calculator.py — Interactive trip calculator

print("=== Road Trip Budget Planner ===")

# Ask the user for *

destination = input("\nEnter your destination: ")
distance = float(input("Enter the distance to your destination (in miles): "))
mpg = float(input("Enter your vehicle's fuel efficiency (miles per gallon): "))
gas_price = float(input("Enter the current price of gas (per gallon): "))
nights = int(input("Enter the number of nights you will stay: "))
hotel_cost = float(input("Enter the cost per night for your hotel: "))
food_budget = float(input("Enter your daily food budget: "))

# Calculate:

gallons = distance / mpg
total_gas_cost = gallons * gas_price
total_hotel_cost = nights * hotel_cost
total_food_cost = (nights + 1) * food_budget
grand_total = total_gas_cost + total_hotel_cost + total_food_cost

# Display the results
print("\n=== Road Trip Budget Planner ===")
print("\nDestination: ", destination)
print(f"Distance: {distance} miles")
print("\n--- Cost Breakdown ---")
print(f"Gas: ({gallons:.2f} gal @ ${gas_price:.2f}/gal): ${total_gas_cost:.2f}")
# hotel cost
print(f"Hotel: ({nights} nights @ ${hotel_cost:.2f}): ${total_hotel_cost:.2f}")
# food cost
print(f"Food: ({nights + 1} days @ ${food_budget:.2f}): ${total_food_cost:.2f}")
print("-" * 30)
print(f"\nEstimated Total: ${grand_total:.2f}")
