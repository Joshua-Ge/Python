from math import sqrt

class quadratic:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.answer1 = 0
        self.answer2 = 0
        self.discre = 0

    def varUpdate(self):
        print("ax^2 + bx + c")
        self.a = input("What is a for the quadratic? >> ")
        self.b = input("What is the b in your quadratic? >> ")
        self.c = input("What is c in your quadratic? >> ")

    def numbering(self):
        self.a = int(self.a)
        self.b = int(self.b)
        self.c = int(self.c)

    def descriminant(self):
        self.discre = (self.b ** 2) - (4 * self.a * self.c)

    def answer(self):
        if self.discre < 0:
            print("The result is imaginary")
        elif self.discre == 0:
            if self.a != 0:
                self.answer1 = ((self.b) ** 2 + sqrt(self.discre)) / (2 * self.a)
                self.answer2 = ((self.b) ** 2 - sqrt(self.discre)) / (2 * self.a)
            else:
                print("You can't have a quadratic that has a = to zero")
        elif self.discre > 0:
            if self.a != 0:
                self.answer1 = ((self.b) ** 2 + sqrt(self.discre)) / (2 * self.a)
                self.answer2 = ((self.b) ** 2 - sqrt(self.discre)) / (2 * self.a)
            else:
                print("You can't have a quadratic that has a = to zero")
        else:
            print("Error")
            
    def answering(self):
        print(f"x is equal to {self.answer1} or {self.answer2}")

num = quadratic()

num.varUpdate()
num.numbering()
num.descriminant()
print(num.discre)
num.answer()
num.answering()