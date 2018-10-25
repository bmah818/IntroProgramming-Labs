# CMPT 120 - Lab #6
# Brya Mah
# 10/25/2018
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', power, and 'quit'.\n")

def inputNumber():
    global num1, num2
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")
    
def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ")
        cmd = cmd.lower()
        
        if cmd == "add":
            inputNumber()
            result = num1 + num2
        elif cmd == "sub":
            inputNumber()
            result = num1 - num2
        elif cmd == "mult":
            inputNumber()
            result = num1 * num2
        elif cmd == "div":
            inputNumber()
            result = num1 // num2
        elif cmd == "power":
            inputNumber()
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
