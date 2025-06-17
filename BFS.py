mazes = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "X", " ", "#", " ", " ", " ", " ", " ", "*", "#"],
         ["#", " ", " ", "#", " ", "#", "#", " ", "#", " ", "#"],
         ["#", " ", "#", "#", " ", "#", " ", " ", "#", " ", "#"],
         ["#", " ", "#", " ", " ", "#", " ", "#", "#", " ", "#"],
         ["#", " ", "#", " ", "#", "#", " ", "#", " ", " ", "#"],
         ["#", " ", " ", " ", "#", " ", " ", "#", " ", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

class maze():
    def __init__(self, maze:object):
        self.maze = maze
        self.start = self.find_symbole("X")
        self.goal = self.find_symbole("*")
        self.history = set()
        self.history.add(self.start)
        self.queue = []
        self.win = False

    def find_symbole(self, symbole):
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if cell == symbole:
                    return f"{j},{i}"
        return None

    def initisateXY(self):
        self.x , self.y = self.start.split(",")
        self.x = int(self.x)
        self.y = int(self.y)

    def bfs(self):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dx,dy in directions:
            newX = self.x + dx
            newY = self.y + dy
            if self.maze[newY][newX] == " ":
                self.queue.append(f"{newX},{newY}")
                self.history.add(f"{newX},{newY}")
            elif self.maze[newY][newX] == "*":
                self.win = True

    def move(self):
        move = self.queue.pop(0)
        x, y = move.split(",")
        x, y = int(x), int(y)
        self.maze[y][x] = "X"
        self.y, self.x = y, x
        
    def display(self):
        print()
        for i, row in enumerate(self.maze):
            print(*row)
        print()

search = maze(mazes)
search.initisateXY()
num = 0
while search.win == False:
    answer = input("Next?")
    num = num + 1
    if answer == "y":
        print(num)
        search.display()
        search.bfs()
        search.move()
        search.display()


