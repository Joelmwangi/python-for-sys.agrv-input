# Name: Dierra Martin
# Due Date: 30/8/2024
# Assignment: M1 Assign 1
# Problem Number: 7

import sys

# Get the input gallons from command-line arguments
gallons = float(sys.argv[1])

# Convert gallons to liters
liters = gallons * 3.78541

# Format liters with 3 decimal places
liters = round(liters, 3)

# Print the output
print(f"{gallons} gallon(US) is equal to {liters} liter")
