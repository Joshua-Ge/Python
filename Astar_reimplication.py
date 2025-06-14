maze = [
    ["X", "1", "1", "5", "W", "2", "2", "3", "4", "5"],
    ["2", "W", "W", "1", "W", "1", "W", "W", "3", "4"],
    ["3", "4", "1", "1", "2", "1", "2", "3", "W", "5"],
    ["4", "W", "2", "W", "3", "W", "4", "W", "W", "1"],
    ["5", "2", "1", "2", "3", "4", "W", "1", "2", "3"],
    ["W", "W", "W", "W", "1", "W", "3", "W", "4", "W"],
    ["3", "2", "1", "1", "1", "2", "2", "2", "1", "0"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "1", "W"],
    ["3", "3", "2", "1", "0", "1", "2", "3", "1", "2"],
    ["4", "5", "4", "3", "2", "3", "4", "5", "4", "*"]
]



class Maze():
    def __init__(self, maze):
        self.maze = maze
        self.start = self.find_char("X")
        self.goal = self.find_char("*")
        self.visited = set()
        self.goalx, self.goaly = self.goal
        self.x, self.y = self.start
        self.path = {}
        self.g_score = {self.start: 0}

    def find_char(self, charecter:str):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == charecter:
                    return (x,y)
                
    def manhatten(self,x,y):
        return (abs(x - self.goalx) + abs(y - self.goaly))
    
    def in_bounds(self,x,y):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])
    
    def Astar(self):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        h = self.manhatten(self.x,self.y)
        moveL = [(h,0,(self.x,self.y))]

        while moveL:

            moveL.sort(reverse=True)

            f,g,spot = moveL.pop()

            if spot == self.goal:
                print("solved")
                cx, cy = spot
                while (cx, cy) != self.start:
                    self.maze[cy][cx] = "X"
                    cx,cy = self.path[(cx,cy)]
                return True
            
            x,y = spot

            self.visited.add(spot)

            for dx, dy in directions:
                newx = dx + x
                newy = dy + y

                if not self.in_bounds(newx,newy):
                    continue

                if (newx, newy) in self.visited:
                    continue

                if self.maze[newy][newx] not in "0123456*":
                    continue

                
                cost = 0 if self.maze[newy][newx] == "*" else int(self.maze[newy][newx])
                check_g = cost + g
            

                if check_g < self.g_score.get((newx, newy), float('inf')):
                    self.g_score[(newx, newy)] = check_g
                    f = check_g + self.manhatten(newx, newy)
                    moveL.append((f, check_g, (newx, newy)))
                    self.path[(newx, newy)] = (x, y)
                    
        print("no path found")
        return False

    def show(self):
        print()
        for i, row in enumerate(self.maze):
            print(*row)
        print()

search = Maze(maze)
search.show()
search.Astar()
search.show()