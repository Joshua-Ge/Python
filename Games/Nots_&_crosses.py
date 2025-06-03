turn = 0

player_map = [
    [" ", " ", "1", " ", "2", " ", "3", " "],
    [" ", "-", "-", "-", "-", "-", "-", "-"],
    ["1", "|", "#", "|", "#", "|", "#", "|"],
    [" ", "-", "-", "-", "-", "-", "-", "-"],
    ["2", "|", "#", "|", "#", "|", "#", "|"],
    [" ", "-", "-", "-", "-", "-", "-", "-"],
    ["3", "|", "#", "|", "#", "|", "#", "|"],
    [" ", "-", "-", "-", "-", "-", "-", "-"]
]

def game_instruts():
    info = ["The # are blank spaces",
            "The way you enter a value is by typing in it's coordanits",
            "An example of coordinates would be, for the top right hands side's corner its location would be 1,1",
            "To type this as a command you would write 'move 'x','y''"]
    
    
    for i in info:
        print(i)

def make_a_move():
    pass

playing = True

while playing == True:
    action = input("What would you like to do? >> ")
    turn += 1

    action = action.strip().lower()

    if action.startswith("move "):
        location = action.removeprefix("move ")
        location = location.split(",")
        x,y = location
        x,y = int(x),int(y)
        x,y = x*2,y*2
        print("moved")
        print(x,y)

        if player_map[y][x] == '#':
            if turn % 2 == 1:
                player_map[y][x] = "X"
            else:
                player_map[y][x] = "0"
        else:
            print("You cheated: Loss of turn")

    elif action == "quit":
        playing = False
    else: 
        print("Please enter a valid option")

    print(*player_map[0])
    print(*player_map[1])
    print(*player_map[2])
    print(*player_map[3])
    print(*player_map[4])
    print(*player_map[5])
    print(*player_map[6])
    print(*player_map[7])
    

