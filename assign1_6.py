# Name: Dierra Martin
# Due Date: 30/8/2024
# Assignment: M1 Assign 1
# Problem Number: 6

import sys

# Get the input hours and rate from command-line arguments
hours = float(sys.argv[1])
rate = float(sys.argv[2])

# Calculate the gross pay
gross_pay = hours * rate

# Format the gross pay with 2 decimal places
gross_pay = round(gross_pay, 2)

# Print the output
print(f"The gross pay for {hours} hours of ${rate} per hour is ${gross_pay}.")
