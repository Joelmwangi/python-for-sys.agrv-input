# Name: Dierra Martin
# Due Date: 30/8/2024
# Assignment: M1 Assign 1
# Problem Number: 2

#importing sys
import sys

# Ensure the correct number of arguments is provided
if len(sys.argv) != 5:
    print("Usage: python script.py <Grade 1> <Grade 2> <Grade 3> <Grade 4>")
    sys.exit(1)

# Get the input grades from command-line arguments
grade1 = int(sys.argv[1])
grade2 = int(sys.argv[2])
grade3 = int(sys.argv[3])
grade4 = int(sys.argv[4])

# Calculate the average
average = (grade1 + grade2 + grade3 + grade4) / 4

# Round the average to 2 decimal places
average = round(average, 2)

# Print the output
print("Grades:", grade1, grade2, grade3, grade4, sep=", ")
print("Average:", average)
