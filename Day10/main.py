'''Día 10. Calculadora:

- El usuario ingresa dos números y un operador (+, -, *, /).
- Se realiza la operación usando funciones almacenadas en un diccionario.
- Se muestra el resultado y se pregunta si desea continuar con ese resultado o empezar de nuevo.'''

from art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    
    print(logo)

    should_accumulate = True
    num1 = float(input("What is the first number: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            clear()
            calculator()

calculator()