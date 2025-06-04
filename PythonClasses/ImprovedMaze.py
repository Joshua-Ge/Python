maze = [["-", "-", "-", "-", "-", "-", "-"],
        ["|", "O", "O", "O", "O", "O", "|"],
        ["|", "O", "O", "O", "O", "O", "|"],
        ["|", "O", "O", "*", "O", "O", "|"],
        ["|", "O", "O", "O", "O", "O", "|"],
        ["|", "O", "O", "X", "O", "O", "|"],
        ["-", "-", "-", "-", "-", "-", "-"]]

pos = [3,5]

class mazeNavigation:
    def __init__(self, location:object, maze:object):
        self.x,self.y = location
        self.maze = maze
        self.printing = True

    def up(self):
        if maze[self.y - 1 ][self.x] == "*":
            print("You won")
            self.printing = False
            return False
        elif maze[self.y - 1 ][self.x] == "-":
            print("You can't got that way")
            self.printing = False
            return True
        else:
            print("You Moved")
            maze[self.y][self.x] = "#"
            self.y = self.y - 1
            maze[self.y][self.x] = "X"
            self.printing = True
            return True
    
    def down(self):
        if maze[self.y + 1 ][self.x] == "*":
            print("You won")
            self.printing = False
            return False
        elif maze[self.y + 1 ][self.x] == "-":
            print("You can't got that way")
            self.printing = False
            return True
        else:
            print("You Moved")
            maze[self.y][self.x] = "#"
            self.y = self.y + 1
            maze[self.y][self.x] = "X"
            self.printing = True
            return True
        
    def left(self):
        if maze[self.y][self.x - 1] == "*":
            print("You won")
            self.printing = False
            return False
        elif maze[self.y][self.x - 1] == "-":
            print("You can't got that way")
            self.printing = False
            return True
        else:
            print("You Moved")
            maze[self.y][self.x] = "#"
            self.x = self.x - 1
            maze[self.y][self.x] = "X"
            self.printing = True     
            return True  

    def right(self):
        if maze[self.y][self.x + 1] == "*":
            print("You won")
            self.printing = False
            return False
        elif maze[self.y][self.x + 1] == "-":
            print("You can't got that way")
            self.printing = False
            return True
        else:
            print("You Moved")
            maze[self.y][self.x] = "#"
            self.x = self.x + 1
            maze[self.y][self.x] = "X"
            self.printing = True
            return True

    def showMaze(self):
        print(*self.maze[0])
        print(*self.maze[1])
        print(*self.maze[2])
        print(*self.maze[3])
        print(*self.maze[4])
        print(*self.maze[5])
        print(*self.maze[6])

    def play(self):
        playing = True

        while playing == True: 
            move = 0
            move = input("Which direction do you want to move (W,A,S,D,Quit) >> ").strip().lower()        

        
            if move == "w":
                playing = self.up()
            elif move == "s":
                playing = self.down()
            elif move == "a":
                playing = self.left()
            elif move == "d":
                playing = self.right()
            elif move == "quit":
                playing = False
                self.printing = False
            else:
                print("Error")

            if self.printing == True:
                self.showMaze()

game1 = mazeNavigation(pos,maze)

game1.play()
        