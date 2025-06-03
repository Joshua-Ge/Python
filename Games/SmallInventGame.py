"""Basic inventory game nothing more"""

invent = []

room_invent = ["food", "water", "ice", "snow", "ice"]

playing = 'yes'

def take_item(item):
    pos = room_invent.index(item)
    room_invent.pop(pos)
    invent.append(item)
    print("Your Inventory: ", invent, "The Room's Inventory: ", room_invent)

def drop_item(item):
    pos = invent.index(item)
    invent.pop(pos)
    room_invent.append(item)
    print("Your Inventory: ", invent, "The Room's Inventory: ", room_invent)

while playing == 'yes':
    answer = input("what will you do? >> ")

    if answer == 'look':
        print(*room_invent)
    elif answer == 'i':
        print("Your inventory contains ", *invent)
    elif answer.startswith('take'):
        thing = answer.removeprefix('take ')
        take_item(thing)
    elif answer.startswith('drop'): 
        thing = answer.removeprefix('drop ')
        drop_item(thing)
    elif answer == 'quit':
        print("leaving so soon?")
        print("bye...")
        playing = 'no'
    else:
        print("Sorry I couldn't understand that")

