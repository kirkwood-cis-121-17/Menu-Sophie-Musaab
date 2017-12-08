# A program

def main():
    print("Welcome to the simple calculator")
    nc = True
    mc = True
    infin = True
    
    while infin:
        while nc:
            mc = True
            try:
                number = float(input("Input your number: "))
                nc = False
            except ValueError:
                print("Try again")
    
       
        while mc: # Chosing the choice from the menu
            menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice <= 0 and choice >= 6:
                    a = 1/0
            except:
                print("Try again")
        
            if choice == 1: # Using the choice to open a function
                
                number = ADDITION(number)
                print (number)
                
            elif choice == 2:
                number = SUBTRACTION(number)
                print (number)
                
            elif choice == 3:
                number = MULTIPLICATION(number)
                print (number)
                
            elif choice == 4:
                number = DIVISION(number)
                print (number)

            elif choice == 5:
                print("Exiting the program...")
                quit()
                
            elif choice == 6:
                nc = True
                mc = False
            else:
                print("Error: Invalid selection.")
                continue
    
def menu():
    print("What do you wish to do with your number")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Close Calculator")
    print("6) New Number")
    
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