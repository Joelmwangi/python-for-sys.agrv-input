# Name: Dierra Martin
# Due Date: 30/8/2024
# Assignment: M1 Assign 1
# Problem Number: 5

#importing sys 
import sys

def main():
    try:
        # Ensure the correct number of arguments are provided
        if len(sys.argv) != 3:
            raise ValueError("Please provide exactly two arguments: an integer and a float.")
        
        # Get the input numbers from command-line arguments
        number1 = int(sys.argv[1])
        number2 = float(sys.argv[2])

        # Print the input numbers
        print(f"Number1 is {number1}")
        print(f"Number2 is {number2}")

        # Perform various calculations and print results with types
        print(f"{number1} // 2 = {number1 // 2} , {type(number1 // 2)}")  # Integer division
        print(f"{number1} / {number2} = {number1 / number2} , {type(number1 / number2)}")  # Floating-point division
        print(f"{number1} * {number2} = {number1 * number2} , {type(number1 * number2)}")  # Multiplication
        print(f"3 ** {number2} = {3 ** number2} , {type(3 ** number2)}")  # Exponentiation

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
