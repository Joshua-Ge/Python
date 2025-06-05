class mathing:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operation = ""
        self.answer = ""
        self.printnow = ""

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 != 0:
            return round(self.num1 / self.num2, 3)
        else:
            return "Dividing by zero is not possible"
    
    def divideRemander(self):
        if self.num2 != 0:
            return f"{round((self.num1 / self.num2) -0.5 , 0)}, and {self.num1 % self.num2}"
        else:
            return "Dividing by zero is not possible"
    
    def exponent(self):
        return self.num1 ** self.num2
    
    def prompt(self):
        self.num1 = int(input("What is your first number? >> "))
        self.num2 = int(input("What is your second number? >> "))

    def helper(self):
        maybe = ["+ : is the symbole used to reprosent adding",
                   "- : is the symbole used to reprosent subtracting",
                   "* : is the symbole used to reprosent multiplying",
                   "/ : is the symbole used to reprosent dividing",
                   "? : is the symbole used to reprosent the help function",
                   "! : is the symbole used to reprosent quit"]
        for i in maybe:
            print(i)
    
    def use(self):
        using = True

        while using == True:
            self.printnow = False
            self.operation = ""
            self.num1 = 0
            self.num2 = 0
            self.operation = input("What operation would you like to do? (+,-,*,/,?,!) >> ").strip()
            if self.operation == "!":
                using = False
            elif self.operation == "+":
                self.prompt()
                self.answer = self.add()
                self.printnow = True
            elif self.operation == "-":
                self.prompt()
                self.answer = self.subtract()
                self.printnow = True
            elif self.operation == "*":
                self.prompt()
                self.answer = self.multiply()
                self.printnow = True
            elif self.operation == "/":
                self.prompt()
                self.answer = self.divide()
                self.printnow = True
            elif self.operation == "?":
                self.helper()
            else:
                print("Please select a correct symbole use '?' for help")

            if self.printnow == True:
                print(f"Your answer is: {self.answer}")
            
                

calculator = mathing()

calculator.use()
