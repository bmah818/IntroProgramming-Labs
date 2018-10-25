# CMPT 120 - Lab #6
# Brya Mah
# 10/25/2018
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', power, and 'quit'.\n")

def inputNumber():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
    except:
        print("You need to enter two numbers. Try again please.")
    return num1, num2
    
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
    
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
        
        if cmd == "add":
            num1,num2 = inputNumber()
            result = num1 + num2
        elif cmd == "sub":
            num1,num2 = inputNumber()
            result = num1 - num2
        elif cmd == "mult":
            num1,num2 = inputNumber()
            result = num1 * num2
        elif cmd == "div":
            num1,num2 = inputNumber()
            result = num1 // num2
        elif cmd == "power":
            num1,num2 = inputNumber()
            result = num1 ** num2
        elif cmd == "quit":
            break
        else:
            print("That is not a valid command")
            continue
        
            
        print("The result is " + str(result) + ".\n")
        
def main():
    showIntro()
    doLoop()
    showOutro()

main()
