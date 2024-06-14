'''
Author: Maaz Ali
Date: May 10, 2024
A Calculator
'''

import art

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1/num2

def multiply(num1, num2):
    return num1*num2

def calculator():
    print(art.logo)
    calculating_flag = True
    operations = {"+": add,
                    "-": subtract,
                    "*": multiply,
                    "/": divide
                    }
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    while calculating_flag:
        operation_input = input("Pick an operation from the line above: ")
        num2 = float(input("Enter the second number: "))
        calculation_choice = operations[operation_input]
        answer = calculation_choice(num1, num2)
        print(f"{num1} {operation_input} {num2} = {answer}")
        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if continue_calc == 'n':
            calculator()
        else:
            num1 = answer

if __name__ == '__main__':
    calculator()