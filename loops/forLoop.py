"""Basic counting game"""

#import datetime

conditioner = input("do you want to count >> ")

while conditioner == "yes":
    #current_time = datetime.time
    count = input("What number do you want to count up to >> ")

    count = int(count.strip())

    for number in range(0,count + 1):
        print(number)
    
    #time_elapsed = datetime.time - current_time

    #print(time_elapsed)