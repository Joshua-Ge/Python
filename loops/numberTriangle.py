"""Basic Pattern made with for loops"""

size = input("How big of a triangle would you like to make? >> ")

size = int(size)

for i in range(0, size + 1):
    print(str(i) * i)