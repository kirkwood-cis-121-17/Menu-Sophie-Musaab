# This is a program that will go through several math processes with the user.

import time

MULTIPLICATION_CHOICE = 1
DIVISION_CHOICE= 2
ADDITION_CHOICE = 3
SUBTRACTION_CHOICE = 4
FACTORIAL_CHOICE = 5
REMAINDER_CHOICE = 6
QUIT_CHOICE = 7


def main():
    
    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Please enter the number of your choice: "))
        handle_choice(choice)
        
def handle_multiplication():
    
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    
    print("\n" + str(num1) + " multiplied by " + str(num2) + " is equal to " + str(num1 * num2) + ".")
    time.sleep(2)
    
def handle_division():
    
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    
    print("\n" + str(num1) + " divided by " + str(num2) + " is equal to " + str(num1 / num2) + ".")
    time.sleep(2)
    
def handle_addition():
    
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    
    print("\n" + str(num1) + " plus " + str(num2) + " is equal to " + str(num1 + num2) + ".")
    time.sleep(2)
    
def handle_subtraction():
    
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    
    print("\n" + str(num1) + " minus " + str(num2) + " is equal to " + str(num1 - num2) + ".")
    time.sleep(2)
    
def get_factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * get_factorial(n-1)
    
def handle_factorial():
    
    num1 = int(input("Please enter your number: "))
    
    fac_num = get_factorial(num1)
    
    print("\n" + str(num1) + " factorial is equal to " + str(fac_num) + ".")
    time.sleep(2)
    
def handle_remainder():
    
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    
    print("\n" + str(num1) + " mod " + str(num2) + " is equal to " + str(num1 % num2) + ".")
    time.sleep(2)
    
def handle_choice(choice):
    if choice == MULTIPLICATION_CHOICE:
        handle_multiplication()
    elif choice == DIVISION_CHOICE:
        handle_division()
    elif choice == ADDITION_CHOICE:
        handle_addition()
    elif choice == SUBTRACTION_CHOICE:
        handle_subtraction()
    elif choice == FACTORIAL_CHOICE:
        handle_factorial()
    elif choice == REMAINDER_CHOICE:
        handle_remainder()
    elif choice == QUIT_CHOICE:
        print("\nExiting the program...\n")
        time.sleep(2)
        print("Thank you!")
        time.sleep(2)
    else:
        print("Error: Invalid selection.")

def display_menu():
    print("\nMENU\n")
    print("1) Multiply")
    print("2) Divide")
    print("3) Add")
    print("4) Subtract")
    print("5) Find Factorial")
    print("6) Find Remainder")
    print("7) Quit\n")
    
main()