class squareRoot():
    def __init__(self):
        self.x = 0.0
        self.n = 0.0
        self.answer = 0.0
        self.reps = 0
    
    def get_input(self):
        self.n = float(input("What number do you want to square root? >> "))
        self.x = self.n/2
        self.reps = int(input("How many times does this repeat? >> "))
    
    def calculate(self):
        self.answer = 0.5 * (self.x + (self.n / self.x))
        self.x = self.answer
    
    def iterate(self):
        for i in range(0, self.reps):
            self.calculate()
            
        print(self.answer)

cont = 'y'
while cont == 'y':         
    calc = squareRoot()
    calc.get_input()
    calc.iterate()
    cont = input("y/n >> ")   