"""Practice with the random python package"""

import random
charecters = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

leng = input("How long do you want your password? >> ")
leng = int(leng.strip())

password = ""

while len(password) <= leng:
    randomLetter = (random.random() * (len(charecters) + 1)) - 1
    randomLetter = round(randomLetter, 0)
    randomLetter = int(randomLetter)
    randomLetter = charecters[randomLetter]
    password = password + randomLetter

print(password)

