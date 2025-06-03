"""Made a cool little game just for fun"""

"""This is the map the user will play on for the game"""
maze = [["-", "-", "-", "-", "-", "-", "-"],
        ["|", "O", "O", "O", "O", "O", "|"],
        ["|", "O", "O", "O", "O", "O", "|"],
        ["|", "O", "O", "*", "O", "O", "|"],
        ["|", "O", "O", "O", "O", "O", "|"],
        ["|", "O", "O", "X", "O", "O", "|"],
        ["-", "-", "-", "-", "-", "-", "-"]]

print(*maze[0])
print(*maze[1])
print(*maze[2])
print(*maze[3])
print(*maze[4])
print(*maze[5])
print(*maze[6])

""" Player start coords which is determine by the location of the X in the 2d list y is inverted and both start at 0 not 1"""
x = 3
y = 5

playing = True # used to determine if the game loop should continue after an action

def move(MOVE:str, xLOC:int, yLOC:int):
    direction = MOVE.upper().strip()
    y = yLOC
    x = xLOC
    cont = True
    do_print = True

    if direction == 'W':
        if maze[y - 1][x] == "*":
            print("You Won")
            do_print = False
            cont = False
        elif maze[y - 1][x] == "-":
            print("Can't Go that way")
            do_print = False
        else:
            print("Moved")
            maze[y][x] = "#"
            y = y - 1
            maze[y][x] = "X"
            do_print = True
    
    elif direction == 'A':
        if maze[y][x - 1] == "*":
            print("You Won")
            do_print = False
            cont = False
        elif maze[y][x - 1] == "|":
            print("Can't Go that way")
            do_print = False
        else:
            print("Moved")
            maze[y][x] = "#"
            x = x - 1
            maze[y][x] = "X"
            do_print = True
    
    elif direction == 'S':
        if maze[y + 1][x] == "*":
            print("You Won")
            do_print = False
            cont = False
        elif maze[y + 1][x] == "-":
            print("Can't Go that way")
            do_print = False
        else:
            print("Moved")
            maze[y][x] = "#"
            y = y + 1
            maze[y][x] = "X"
            do_print = True
    
    elif direction == 'D':
        if maze[y][x + 1] == "*":
            print("You Won")
            do_print = False
            cont = False
        elif maze[y][x + 1] == "|":
            print("Can't Go that way")
            do_print = False
        else:
            print("Moved")
            maze[y][x] = "#"
            x = x + 1
            maze[y][x] = "X"
            do_print = True
    
    else:
        print("Please select a valid option (WASD)")

    return x,y,do_print,cont

while playing:
    action = input("What would you like to do? >> ")

    if action.startswith("move "):
        thing = action.removeprefix("move ")
        x,y,do_print,playing = move(thing,x,y)

    elif action == 'quit':
        playing = False
        do_print = False
    else:
        print("Please pick a valid option")

    if do_print == True:
        print(*maze[0])
        print(*maze[1])
        print(*maze[2])
        print(*maze[3])
        print(*maze[4])
        print(*maze[5])
        print(*maze[6])