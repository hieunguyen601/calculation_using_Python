from art import logo

# Calculator functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

# Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}

# Calculator main function
def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Enter the second number: "))

    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {result}")

    while True:
        next_part = input("Type 'y' to continue calculating with the result, or type 'n' to start a new calculation: ")

        if next_part == 'y':
            operation_symbol = input("Pick another operation: ")
            num3 = float(input("Enter the next number: "))
            calculation_function = operations[operation_symbol]
            result = calculation_function(result, num3)
            print(f"{result}")
        elif next_part == 'n':
            print("Exiting...")
            break
        else:
            print("Invalid input.")

calculator()