from re import split


ground=[["   ", " 1 ", " 2 ", " 3 ", " 4 ", " 5 ", "   ", "   "],
        [" - ", " - ", " - ", " - ", " - ", " - ", " - ", "   "],
        [" | ", " O ", " O ", " O ", " O ", " O ", " | ", " 1 "],
        [" | ", " O ", " O ", " O ", " O ", " O ", " | ", " 2 "],
        [" | ", " O ", " O ", " O ", " O ", " O ", " | ", " 3 "],
        [" | ", " O ", " O ", " O ", " O ", " O ", " | ", " 4 "],
        [" | ", " O ", " O ", " O ", " O ", " O ", " | ", " 5 "],
        [" - ", " - ", " - ", " - ", " - ", " - ", " - ", "   "]]


class plant:
    def __init__(self, name, symbole):
        self.name = name
        self.symbole = symbole

    def describe(self):
        return f"This is a {self.name}"
    
class carrot(plant):
    def __init__(self):
        super().__init__("Carrot", "🥕 ")

class potato(plant):
    def __init__(self):
        super().__init__("Potato", "🥔 ")

class onion(plant):
    def __init__(self):
        super().__init__("Onion", "🧅 ")




seeds = {
    "carrot" : carrot,
    "potato" : potato,
    "onion" : onion
}

class garden:
    def __init__(self, Floor):
        self.floor = Floor
        self.x = 0
        self.y = 0

    def showgarden(self):
        print(*self.floor[0])
        print(*self.floor[1])
        print(*self.floor[2])
        print(*self.floor[3])
        print(*self.floor[4])
        print(*self.floor[5])
        print(*self.floor[6])
        print(*self.floor[7])
        
    def updateGarden(self, location, user_seed):
        self.x, self.y = split(',', location)
        self.x = int(self.x)
        self.y = int(self.y)

        if self.x and self.y in range(1,5):
            if user_seed in seeds:
                plant_class = seeds[user_seed]
                new_plant = plant_class()
                self.x, self.y = split(',', location)
                self.x = int(self.x)
                self.y = int(self.y)
                ground[self.y + 1][self.x] = new_plant.symbole
                print(f"you planted {new_plant.name}")
            else:
                print("Sorry, we dont have that plant")
        else:
            print("That is not a valid location")






gardengame = garden(ground)
playing = True

while playing == True:

    gardengame.showgarden()

    act = input("What will you do? >> ")

    if act == "grow":
        action = input("What would you like to plant, (<PLANT>, <LOCATION>) >> ")

        food, place = split(",",action,1)

        food = food.lower().strip()
        place = place.strip()
    
        gardengame.updateGarden(place,food)
    elif act == "quit":
        playing = False
    else:
        print("Sorry, but that action is not supported")