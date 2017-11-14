# A program

def main():
    
    print("Welcome to the simple calculator")
    
    while True:
        try:
            number = float(input("Input your number: "))
            break
        except ValueError:
            print("Try again")

    menu()
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice > 0 and choice < 6:
                break
        except:
            print("Try again")
    
    if choice == 1:
        print (ADDITION(number))
    elif choice == 2:
        print (SUBTRACTION(number))
    elif choice == 3:
        print (MULTIPLICATION(number))
    elif choice == 4:
        print (DIVISION(number))
    elif choice == 5:
        active = False
        print("Exiting the program...")
    else:
        print("Error: Invalid selection.")
        choice = input("Enter a new choice")
    
def menu():
    print(" What do you wish to do with your number")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Close Calculator")    
    
def ADDITION(orig):
    numb = int(input("Enter the number you want to add to your number: "))
    orig = orig + numb
    return orig

def SUBTRACTION(orig):
    numb = int(input("Enter the number you want to subtract from your number: "))
    orig = orig - numb
    return orig
    
def MULTIPLICATION(orig):
    numb = int(input("Enter the number you want to mulitiply your number by: "))
    orig = orig * numb
    return orig
    
def DIVISION(orig):
    numb = int(input("Enter the number you want to divide your number by: "))
    orig = orig / numb
    return orig

main()