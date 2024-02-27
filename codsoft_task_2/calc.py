def get_float_input(prompt):
    #hadling exception for other than numeric input 
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    # Takeing Operators input(float) and operator
    num1 = get_float_input("Enter the first number: ")
    num2 = get_float_input("Enter the second number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    

    # Used match, which works like switch in C.
    match operator:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            # Check for division by zero
            if num2 != 0:
                result = (num1 / num2)
            else:
                print("Deominator can't be Zero")
                result = None
        case _:
            result = None

    # Display the result or handle invalid operator
    if result is not None:
        print(f"The result of {num1} {operator} {num2} is: {result}")
    else:
        print("Invalid operation. Please enter a valid operator/operands.")

# Calling the Calculator, (Implemented as function , for ease of testing)
calculator()
