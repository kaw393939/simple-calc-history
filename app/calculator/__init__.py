"""
This file contains a simple calculator that can add, subtract, multiply, and divide numbers based on user input.
It now includes a history feature that allows users to view past calculations, clear the history, and undo the last calculation.
"""

# Import the math operations from the operations module.
from app.operations import addition, subtraction, multiplication, division

# Import the History class from the history module.
from app.history import History

def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division, with history support."""

    # Create a History object to manage the history of calculations.
    history = History()

    # Print a welcome message and instructions.
    print("Welcome to the calculator REPL! Type 'exit' to quit.")
    print("You can also type 'history' to view past calculations, 'clear' to clear history, or 'undo' to remove the last calculation.")

    # Start the REPL loop.
    while True:
        # Prompt the user for input.
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: ")

        # Handle the 'exit' command.
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break

        # Handle the 'history' command.
        elif user_input.lower() == "history":
            print("Calculation History:")
            for calc in history.get_history():
                print(calc)
            continue

        # Handle the 'clear' command.
        elif user_input.lower() == "clear":
            history.clear_history()
            print("History cleared.")
            continue

        # Handle the 'undo' command.
        elif user_input.lower() == "undo":
            history.undo_last()
            print("Last calculation undone.")
            continue

        # Process the input as a calculation.
        else:
            try:
                # Try to split the input into operation and numbers.
                operation, num1, num2 = user_input.split()
                num1, num2 = float(num1), float(num2)
            except ValueError:
                # If the input is not in the correct format, show an error message.
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                continue

            # Perform the requested operation.
            if operation == "add":
                result = addition(num1, num2)
            elif operation == "subtract":
                result = subtraction(num1, num2)
            elif operation == "multiply":
                result = multiplication(num1, num2)
            elif operation == "divide":
                try:
                    result = division(num1, num2)
                except ValueError as e:
                    print(e)
                    continue
            else:
                print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide.")
                continue

            # Store the calculation in the history.
            calculation_str = f"{operation} {num1} {num2} = {result}"
            history.add_calculation(calculation_str)

            # Print the result.
            print(f"Result: {result}")
