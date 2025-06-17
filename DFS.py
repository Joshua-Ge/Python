mazes = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "X", " ", "#", " ", " ", " ", " ", " ", "*", "#"],
         ["#", " ", " ", "#", " ", "#", "#", " ", "#", " ", "#"],
         ["#", " ", "#", "#", " ", "#", " ", " ", "#", " ", "#"],
         ["#", " ", "#", " ", " ", "#", " ", "#", "#", " ", "#"],
         ["#", " ", "#", " ", "#", "#", " ", "#", " ", " ", "#"],
         ["#", " ", " ", " ", "#", " ", " ", "#", " ", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]


class maze():
    def __init__(self, mazes:object,):
        self.maze = mazes
        self.start = ""
        self.x = 0
        self.y = 0
        self.stack = []
        self.goal = ""
        self.goalx = 0
        self.goaly = 0
        self.win = False


    def find_start(self):
        for i,row in enumerate(self.maze): # the function enumerate returns the index and the element stored so 1, ["0", "0", "X"]
            for j, cell in enumerate (row): # this time enumerate returns a string since its searching a list so 1, "X"
                if cell == "X":
                    self.start = str(i) + "," + str(j) # this saves the location but as a comma seperated value

    def find_goal(self):
        for i,row in enumerate(self.maze): # the function enumerate returns the index and the element stored so 1, ["0", "0", "X"]
            for j, cell in enumerate (row): # this time enumerate returns a string since its searching a list so 1, "X"
                if cell == "*":
                    self.goal = str(i) + "," + str(j) # this saves the location but as a comma seperated value

    def set_x_y(self):
        self.y, self.x = self.start.split(",")
        self.x = int(self.x)
        self.y = int(self.y)
        
    def set_goal_location(self):
        self.goalx, self.goaly = self.goal.split(',')
        self.goalx = int(self.goalx)
        self.goaly = int(self.goaly)


    def show(self):
        print(self.start)

    def find_options(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            newX, newY = self.x + dx, self.y + dy
            if 0 <= newY < len(self.maze) and 0 <= newX < len(self.maze[0]):
                if self.maze[newY][newX] == " ":
                    print(f"appended {newX},{newY}")
                    self.stack.append(f"{newX},{newY}")
                elif self.maze[newY][newX] == "*":
                    self.win_check()
                    
                

    def move(self):
        print(self.stack)
        move = self.stack.pop(-1)
        print(move)
        x, y = move.split(",")
        x, y = int(x), int(y)
        self.maze[y][x] = "X"            
        self.y, self.x = y, x            
        for i, row in enumerate(self.maze):
            print(*row)

    def win_check(self):
        if self.maze[self.y+1][self.x] == "*":
            print("you won")
            self.win = True
        elif self.maze[self.y-1][self.x] == "*":
            print("you won")
            self.win = True
        elif self.maze[self.y][self.x+1] == "*":
            print("you won")
            self.win = True      
        elif self.maze[self.y][self.x-1] == "*":
            print("you won")
            self.win = True

bob = maze(mazes)
bob.find_start()
bob.find_goal()
bob.show()
bob.set_x_y()
bob.find_goal()

action = ""

while bob.win == False:
        bob.win_check()
        bob.find_options()
        bob.move()
