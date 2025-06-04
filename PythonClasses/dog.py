class dog:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        self.dogyears = age*7
        

    def describe(self):
        print(f"My dogs name is {self.name}, and he is {self.age} years old")
        print(f"My dog is {self.dogyears} in dog years")

my_dog =  dog("Willow", 3)

my_dog.describe()