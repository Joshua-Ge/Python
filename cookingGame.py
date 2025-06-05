inventory = []
room1 = ["pot", "carrot", "potato"]

def salting(nom_nom):
    nom_nom.salting()

class food:
    def __init__(self, name, cutable, boilable, fryable):
        self.name = name
        self.cutable = cutable
        self.boilable = boilable
        self.fryable = fryable
        self.state = self.name.removesuffix(name)
    
    def cut(self):
        if self.cutable == True and not self.name.startswith("cut"):
            self.name = "cut " + self.name
        else: 
            print(f"you can not cut {self.name}")
    
    def boil(self):
        if self.boilable == True and not self.name.startswith("boiled"):
            self.name = "boiled " + self.name
        else: 
            print(f"you can not cut {self.name}")

    def fry(self):
        if self.fryable == True and not self.name.startswith("fried"):
            self.name = "fried " + self.name
        else: 
            print(f"you can not cut {self.name}")
    
    def display_name(self):
        print(self.name)
    
    def salting(self):
        if self.state == "fried" and self.name == "potato":
            self.name = "french fries"


class equipment:
    def __init__(self, name, usecase):
        self.name = name
        self.use = usecase
        self.invent = []
        

class player:
    def __init__(self, name, invent):
        self.name = name
        self.invent  = invent

    def take(self, current_room, item):
        location = current_room.index(item)
        current_room.pop(location)
        self.invent.append(item)

    def drop(self, current_room):
        item = input("what item are you dropping >> ").strip().lower()
        location = current_room.index(item)
        current_room.append(location)
        self.invent.pop(item)

    def add(self, obj):
        item = input(f"What are you adding to {obj.name}? >> ")
        
        for i in self.invent:
            if i == item:
                additem = True
       

        if additem == True:
            obj.invent.append(item) 
            print(obj.invent)
        

    def show(self):
        print(f"{self.name}'s inventory has {self.invent}")

    def use(self):
        item = input("What item do you want to use? >> ").strip().lower()

        Useitem = False

        for i in self.invent:
            if i == item:
                Useitem = True
                print("You can use that item")

        if item == 'pot' and Useitem == True:
            for i in pot.invent:
                if i == "carrot":
                    carrot.boil()
                    carrot.display_name()
                elif i == "potato":
                    potato.boil()
                    potato.display_name()


    


john = player("John", inventory)
carrot = food("carrot", True, True, False)
potato = food("potato", True, True, True)
pot = equipment("pot", "boiling")

playing = True

while playing == True:
    room = room1
    action = 0
    
    print("")
    print(f"The current room has {room} in it")
    print(f"{john.name} Has {john.invent} in their inventory")
    print("")
    
    action = input("What would you like to do? >> ").strip().lower()


    if action.startswith("take "):
        item = action.removeprefix("take ")
        john.take(room, item)
    elif action == "drop":
        john.drop(room)
    elif action == "add":
        obj = input("What are you adding to? >> ")
        if obj == "pot":
            john.add(pot)
        else:
            print("invalid")
    elif action == "show":
        john.show()
    elif action == "use":
        john.use()
    elif action == "clear":
        playing = False
    else:
        print("Please select a valid answer")






