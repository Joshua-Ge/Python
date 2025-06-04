class cat:
    def __init__(self, name:str, age:int, gender:str, ):
        self.name = name
        self.age = age 
        self.catage = age * 7
        self.gender = gender

    def info(self):
        if self.gender == "male":
            print(f"My cats name is {self.name}, He is {self.age}")
            print(f"He is {self.catage} in cat years")
        elif self.gender == "female":
            print(f"My cats name is {self.name}, she is {self.age}")
            print(f"She is {self.catage} in cat years")
        else:
            print("Error")            

cat1 = cat("Fudge", 15, "female")
cat2 = cat("Smudge", 15, "female")
cat3 = cat("Mr.Meowgie", 14, "male")
cat4 = cat("Marshmellow", 2, "male")
cat5 = cat("Cocobella", 15, "female")

cat1.info()
cat2.info()
cat3.info()
cat4.info()
cat5.info()

