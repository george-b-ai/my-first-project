# number_collector.py — Handles bad input gracefully
print("=" * 30)
print("    number_collector")
print("=" * 30)
# Get number_collector with error handling
try:
    number1 = int(input("Enter the first number: "))
except ValueError:
    number1 = 0
try:
        number2 = int(input("Enter the second number: "))
except ValueError:
        number2 = 0
try:
            number3 = int(input("Enter the third number: "))
except ValueError:
            number3 = 0
print("\nYour numbers: ", number1, number2, number3)
print("Sum: ", number1 + number2 + number3)
average = (number1 + number2 + number3) / 3
print("Average: ", f"{average:.2f}")