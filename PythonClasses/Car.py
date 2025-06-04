class car:
    def __init__(self, make:str, model:str, year:int, gas:int):
        self.make = make
        self.model = model
        self.year = year
        self.gas = gas
        self.full = 100

    def start_engine(self):
        print("engine started")

    def showInfo(self):
        print(f"The make is {self.make}")
        print(f"The model is {self.model}")
        print(f"The year of the cars manufacture is {self.year}")

    def drive(self):
        self.gas -= 10
        print(f"Your tank is at {self.gas}")

    def refuel(self):
        self.gas = self.full
        print(f"Your tank is at {self.gas}")

Car = car("Toyota", "Rav-4", 2020, 50)


Car.showInfo()
Car.drive()
Car.drive()
Car.drive()
Car.drive()
Car.drive()
Car.refuel()