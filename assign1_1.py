# Name: Dierra Martin
# Due Date: 30/8/2024
# Assignment: M1 Assign 1
# Problem Number: 1

# importing sys 
import sys

# Ensure the correct number of arguments is provided
if len(sys.argv) != 4:
    print("Usage: python assign1_1.py <First Name> <Last Name> <GPA>")
    sys.exit(1)

# Get the input name and GPA from command-line arguments
first_name = sys.argv[1]
last_name = sys.argv[2]
gpa = float(sys.argv[3])

# Print the output
print("First Name:", first_name)
print("Last Name:", last_name)
print("GPA: {:.2f}".format(gpa))
