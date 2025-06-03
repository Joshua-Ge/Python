"""Simple calculator to practice variable typing"""

def add():
    location = "add"
    num1 = input("What is your first number (enter quit to leave)>> ")
    num1.lower().strip()
    if num1 == "quit":
        location = "main"    
    while location == "add":
        num2 = input("What is your second number >> ")
        num1 = float(num1.strip())
        num2 = float(num2.strip())
        result = num1 + num2
        print(result)

def subtract(): 
    location = "sub"
    num1 = input("What is your first number (enter quit to leave)>> ")
    num1.lower().strip()
    if num1 == "quit":
        location = "main"    
    while location == "sub":
        num2 = input("What is your second number >> ")
        num1 = float(num1.strip())
        num2 = float(num2.strip())
        result = num1 - num2
        print(result)

def multiply():
    location = "multi"
    num1 = input("What is your first number (enter quit to leave)>> ")
    num1.lower().strip()
    if num1 == "quit":
        location = "main"    
    while location == "multi":
        num2 = input("What is your second number >> ")
        num1 = float(num1.strip())
        num2 = float(num2.strip())
        result = num1 * num2
        print(result)

def division():
    location = "divison"
    num1 = input("What is your first number (enter quit to leave)>> ")
    num1.lower().strip()
    if num1 == "quit":
        location = "main"    
    while location == "divison":
        num2 = input("What is your second number >> ")
        num1 = float(num1.strip())
        num2 = float(num2.strip())
        result = num1 / num2
        print(result)

def remainder():
    location = "remaind"
    num1 = input("What is your first number (enter quit to leave)>> ")
    num1.lower().strip()
    if num1 == "quit":
        location = "main"    
    while location == "remaind":
        num2 = input("What is your second number >> ")
        num1 = float(num1.strip())
        num2 = float(num2.strip())
        result = num1 % num2
        print(result)

def exponent():
    location = "exponent"
    num1 = input("What is your first number (enter quit to leave)>> ")
    num1.lower().strip()
    if num1 == "quit":
        location = "main"    
    while location == "exponent":
        num2 = input("What is your second number >> ")
        num1 = float(num1.strip())
        num2 = float(num2.strip())
        result = num1 ** num2
        print(result)

if __name__ == "__main__":
    location =  "main"
    while location == "main":
        action = input("What would you like to do (+,-,*,/) >> ")
        action = action.lower().strip()
        if action == "+":
            add()
        elif action == "-":
            subtract()
        elif action == "*":
            multiply()
        elif action == "/":
            division()
        elif action == "%":
            remainder()
        elif action == "^":
            exponent()
        elif action == "quit":
            location = 0
        else:
            print("Invalid response")
    
    print("program ending")
        