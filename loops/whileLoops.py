"""Just a simple program to practice the basic syntax of while loops"""

response = input("Do you like this program >> ")

response = response.strip().lower()

while response == "yes":
    question = input("Do you like this program >> ")
    question = question.strip().lower()
    if question == "yes":
        while True:
            print("YOU DO")
    else:
        print("Why not...")

print("Bye...")