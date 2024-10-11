# **Simple Calculator with History Feature**

This guide explains how to build a simple command-line calculator in Python that performs basic arithmetic operations and includes a history feature. The calculator supports addition, subtraction, multiplication, and division. It also allows users to view past calculations, clear the history, and undo the last calculation.

## **Table of Contents**

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Main Program (`main.py`)](#main-program-mainpy)
4. [Calculator Module (`app/calculator/__init__.py`)](#calculator-module-appcalculatorinitpy)
5. [Operations Module (`app/operations/__init__.py`)](#operations-module-appoperationsinitpy)
6. [History Module (`app/history/__init__.py`)](#history-module-apphistoryinitpy)
7. [Running the Calculator](#running-the-calculator)
8. [Additional Resources](#additional-resources)

---

## **Introduction**

This calculator program is designed to teach students how to build a modular Python application using functions, classes, and modules. By following this guide, you'll learn how to:

- Organize code using modules and packages.
- Implement basic arithmetic operations using functions.
- Use a class to manage the history of calculations.
- Interact with users through a command-line interface.
- Handle errors and provide user-friendly messages.

---

## **Project Structure**

The project is organized into the following files and directories:

```
calculator_project/
├── main.py
└── app/
    ├── calculator/
    │   └── __init__.py
    ├── operations/
    │   └── __init__.py
    └── history/
        └── __init__.py
```

- **`main.py`**: The entry point of the program.
- **`app/calculator/__init__.py`**: Contains the main calculator logic.
- **`app/operations/__init__.py`**: Defines arithmetic operation functions.
- **`app/history/__init__.py`**: Manages the history of calculations.

---

## **Main Program (`main.py`)**

The `main.py` file serves as the entry point to start the calculator. It imports the `calculator` function from the `app.calculator` module and runs it when the script is executed directly.

**Code Example:**

```python
# Import the calculator function from the calculator module
from app.calculator import calculator

# Check if the script is run directly and start the calculator
if __name__ == "__main__":
    calculator()
```

**Explanation:**

- **Import Statement:**
  ```python
  from app.calculator import calculator
  ```
  This line imports the `calculator` function, which contains the main loop of our calculator program.

- **Main Guard:**
  ```python
  if __name__ == "__main__":
      calculator()
  ```
  The `if __name__ == "__main__":` condition checks if the script is being run directly. If so, it calls the `calculator()` function to start the program.

**Further Reading:**

- [Python Modules and Packages](https://docs.python.org/3/tutorial/modules.html)
- [The `__name__` Variable](https://docs.python.org/3/library/__main__.html)

---

## **Calculator Module (`app/calculator/__init__.py`)**

The `calculator` module contains the main logic for the calculator, including handling user input, performing calculations, and managing the history.

**Code Example:**

```python
# Import necessary modules and classes
from app.operations import addition, subtraction, multiplication, division
from app.history import History

def calculator():
    """Basic REPL calculator with history support."""

    # Create a History object
    history = History()

    # Welcome message
    print("Welcome to the calculator REPL! Type 'exit' to quit.")
    print("You can also type 'history' to view past calculations, 'clear' to clear history, or 'undo' to remove the last calculation.")

    # Start the REPL loop
    while True:
        user_input = input("Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: ")

        # Handle special commands
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break
        elif user_input.lower() == "history":
            print("Calculation History:")
            for calc in history.get_history():
                print(calc)
            continue
        elif user_input.lower() == "clear":
            history.clear_history()
            print("History cleared.")
            continue
        elif user_input.lower() == "undo":
            history.undo_last()
            print("Last calculation undone.")
            continue

        # Process calculation input
        else:
            try:
                operation, num1, num2 = user_input.split()
                num1, num2 = float(num1), float(num2)
            except ValueError:
                print("Invalid input. Please follow the format: <operation> <num1> <num2>")
                continue

            # Perform the requested operation
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

            # Store the calculation in history
            calculation_str = f"{operation} {num1} {num2} = {result}"
            history.add_calculation(calculation_str)

            # Display the result
            print(f"Result: {result}")
```

**Explanation:**

- **Imports:**
  ```python
  from app.operations import addition, subtraction, multiplication, division
  from app.history import History
  ```
  - Import arithmetic functions from the `operations` module.
  - Import the `History` class from the `history` module.

- **`calculator` Function:**
  - Initializes a `History` object to manage calculations.
  - Prints welcome messages and instructions.
  - Enters an infinite loop to process user input.

- **Handling Special Commands:**
  - **`exit`**: Exits the calculator.
  - **`history`**: Displays all past calculations.
  - **`clear`**: Clears the calculation history.
  - **`undo`**: Removes the last calculation from history.

- **Processing Calculations:**
  - Splits user input into operation and operands.
  - Converts operands to floats.
  - Performs the requested operation using the corresponding function.
  - Handles division by zero errors.
  - Stores the calculation in history.
  - Displays the result.

**Further Reading:**

- [Input and Output in Python](https://docs.python.org/3/tutorial/inputoutput.html)
- [Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
- [Exceptions Handling](https://docs.python.org/3/tutorial/errors.html)

---

## **Operations Module (`app/operations/__init__.py`)**

The `operations` module defines four basic arithmetic functions: addition, subtraction, multiplication, and division.

**Code Example:**

```python
def addition(a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a + b

def subtraction(a: float, b: float) -> float:
    """Subtracts the second number from the first and returns the result."""
    return a - b

def multiplication(a: float, b: float) -> float:
    """Multiplies two numbers and returns the result."""
    return a * b

def division(a: float, b: float) -> float:
    """Divides the first number by the second and returns the result."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
```

**Explanation:**

- **Type Annotations:**
  - The functions use type annotations to specify that both parameters and return values are floats.
  - Example: `def addition(a: float, b: float) -> float:`

- **Arithmetic Functions:**
  - **`addition`**: Returns the sum of `a` and `b`.
  - **`subtraction`**: Returns the difference between `a` and `b`.
  - **`multiplication`**: Returns the product of `a` and `b`.
  - **`division`**: Returns the quotient of `a` divided by `b`. Raises a `ValueError` if `b` is zero.

**Further Reading:**

- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Type Annotations](https://docs.python.org/3/library/typing.html)
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

---

## **History Module (`app/history/__init__.py`)**

The `history` module contains the `History` class, which manages a list of calculations. It provides methods to add, clear, undo, and retrieve calculations.

**Code Example:**

```python
class History:
    """Class to manage the history of calculations."""

    def __init__(self):
        # Initialize an empty list to store calculations
        self.calculations = []

    def add_calculation(self, calculation: str):
        """
        Adds a calculation to the history.
        :param calculation: String representation of the calculation.
        """
        self.calculations.append(calculation)

    def clear_history(self):
        """Clears all calculations from the history."""
        self.calculations.clear()

    def undo_last(self):
        """Removes the last calculation from the history."""
        if self.calculations:
            self.calculations.pop()
        else:
            print("History is already empty.")

    def get_history(self):
        """
        Retrieves the list of calculations.
        :return: List of calculations.
        """
        return self.calculations
```

**Explanation:**

- **`__init__` Method:**
  - Initializes an empty list `self.calculations` to store calculation history.

- **Methods:**
  - **`add_calculation`**: Adds a calculation string to the history list.
  - **`clear_history`**: Clears the history list.
  - **`undo_last`**: Removes the last calculation from the history list.
  - **`get_history`**: Returns the current history list.

- **Error Handling:**
  - In `undo_last`, checks if the history is empty before attempting to remove the last item.

**Further Reading:**

- [Classes in Python](https://docs.python.org/3/tutorial/classes.html)
- [Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Docstrings](https://www.python.org/dev/peps/pep-0257/)

---

## **Running the Calculator**

To run the calculator program, follow these steps:

1. **Navigate to the Project Directory:**
   ```bash
   cd calculator_project
   ```

2. **Run the `main.py` Script:**
   ```bash
   python main.py
   ```

3. **Using the Calculator:**

   - **Perform a Calculation:**
     - Enter an operation followed by two numbers.
     - Format: `<operation> <num1> <num2>`
     - Example:
       ```
       add 5 3
       ```

   - **View History:**
     - Type `history` to display all past calculations.

   - **Clear History:**
     - Type `clear` to remove all calculations from history.

   - **Undo Last Calculation:**
     - Type `undo` to remove the last calculation from history.

   - **Exit the Calculator:**
     - Type `exit` to quit the program.

**Sample Session:**

```
Welcome to the calculator REPL! Type 'exit' to quit.
You can also type 'history' to view past calculations, 'clear' to clear history, or 'undo' to remove the last calculation.
Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: add 10 5
Result: 15.0
Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: multiply 2 3
Result: 6.0
Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: history
Calculation History:
add 10.0 5.0 = 15.0
multiply 2.0 3.0 = 6.0
Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: undo
Last calculation undone.
Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: history
Calculation History:
add 10.0 5.0 = 15.0
Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: clear
History cleared.
Enter an operation (add, subtract, multiply, divide) and two numbers, or a command: exit
Exiting calculator...
```

---

## **Additional Resources**

To deepen your understanding of the concepts used in this program, you can refer to the following resources from the Python documentation:

- **Modules and Packages:**
  - [Python Modules](https://docs.python.org/3/tutorial/modules.html)
  - [Packages in Python](https://docs.python.org/3/tutorial/modules.html#packages)
  
- **Input and Output:**
  - [The `input()` Function](https://docs.python.org/3/library/functions.html#input)
  - [Formatted String Literals (f-strings)](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
  
- **Control Flow:**
  - [`if` Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
  - [Loops (`while` and `for`)](https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools)
  
- **Error Handling:**
  - [Exceptions](https://docs.python.org/3/tutorial/errors.html)
  - [`try` and `except` Statements](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
  
- **Functions:**
  - [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
  - [Function Annotations](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)
  
- **Classes and Objects:**
  - [Classes](https://docs.python.org/3/tutorial/classes.html)
  - [Instance Objects](https://docs.python.org/3/tutorial/classes.html#instance-objects)
  
- **Data Structures:**
  - [Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
  - [List Methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

---

By studying this guide and experimenting with the code, you'll gain practical experience in building Python applications with modular code organization, user interaction, and basic data management. Feel free to modify and expand the program to include additional features or operations to further enhance your learning.