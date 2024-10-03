#Create a functions for each operation

import math 

def exponentiate(x,y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def percentage(x, percent):
    return (x * percent) / 100

#User input and display the menu

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiation (x^y)")
    print("6. Square Root (√x)")
    print("7. percent")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            if choice == '6': #Square root only takes one input
                num1 = float(input("Enter a number: "))
                print(f"√{num1} = {square_root(num1)}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply (num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")  
                elif choice == '5':
                    print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")    
                elif choice == '7':
                    num = float(input("Enter the number"))
                    percent= float(input("Enter the percentage"))
                    print(f"{percent}% of {num} = {percentage(num, percent)}")

        else:
            print("Invalid input. Please choose a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break


if __name__ == "__main__":
    calculator()        