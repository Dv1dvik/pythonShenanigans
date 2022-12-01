from art import logo

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    end = False
    num1 = float(input("What is the first number?: "))
    while not end:
        #Choosing operation
        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))

        #calculation
        calculation = operations[operation_symbol]
        answer = (calculation(num1, num2))
        #Output
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        end_input = input(f"Type 'y' for continue calculation with {answer}, and if you want to start a new calculation type 'n': ").lower()
        #Continue or not
        if end_input == "y":
            num1 = answer
        elif end_input == "n":
            end = True
            calculator()

calculator()