# Name: Dierra Martin
# Due Date: 30/8/2024
# Assignment: M1 Assign 1
# Problem Number: 4

# importing sys
import sys

# Ensure the correct number of arguments is provided
if len(sys.argv) != 5:
    print("Usage: python script.py <Principal> <Interest Rate (%)> <Payments Per Year> <Total Years>")
    sys.exit(1)

# Get the input values from command-line arguments
principal = float(sys.argv[1])
interest_rate = float(sys.argv[2])
payments_per_year = int(sys.argv[3])
total_years = int(sys.argv[4])

# Convert interest rate to a decimal
interest_rate = interest_rate / 100

# Calculate the total amount accrued using the compound interest formula
total_amount = principal * (1 + interest_rate / payments_per_year) ** (payments_per_year * total_years)

# Calculate the interest paid
interest_paid = total_amount - principal

# Format the interest paid with 1 decimal place
interest_paid = round(interest_paid, 1)

# Print the output
print("Interest Paid: $", interest_paid)
