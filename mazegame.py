import tkinter as tk
import random

class MazeSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Convoluted Maze Solver")

        self.canvas = tk.Canvas(self.master, width=400, height=400, borderwidth=0, highlightthickness=0)
        self.canvas.pack()

        self.generate_button = tk.Button(self.master, text="Generate Maze", command=self.generate_maze)
        self.generate_button.pack()

        self.solve_button = tk.Button(self.master, text="Solve Maze", command=self.solve_maze)
        self.solve_button.pack()

        self.maze_size = 10
        self.maze = None
        self.start = (0, 0)
        self.end = (self.maze_size - 1, self.maze_size - 1)

    def generate_maze(self):
        self.canvas.delete("all")
        self.maze = [[random.randint(0, 1) for _ in range(self.maze_size)] for _ in range(self.maze_size)]
        self.draw_maze()

    def draw_maze(self):
        cell_width = 400 // self.maze_size
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                x0, y0 = j * cell_width, i * cell_width
                x1, y1 = x0 + cell_width, y0 + cell_width
                if self.maze[i][j] == 1:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="black")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")

    def solve_maze(self):
        if not self.maze:
            return

        visited = set()
        path = []

        def dfs(current):
            if current == self.end:
                return True

            visited.add(current)
            x, y = current

            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            random.shuffle(neighbors)

            for neighbor in neighbors:
                nx, ny = neighbor
                if 0 <= nx < self.maze_size and 0 <= ny < self.maze_size and self.maze[nx][ny] == 0 and neighbor not in visited:
                    path.append(neighbor)
                    if dfs(neighbor):
                        return True
                    path.pop()

            return False

        if dfs(self.start):
            for step in path:
                x, y = step
                x0, y0 = y * (400 // self.maze_size), x * (400 // self.maze_size)
                x1, y1 = x0 + (400 // self.maze_size), y0 + (400 // self.maze_size)
                self.canvas.create_rectangle(x0, y0, x1, y1, fill="green")
        else:
            print("No solution found!")

def main():
    root = tk.Tk()
    app = MazeSolver(root)
    root.mainloop()

if __name__ == "__main__":
    main()
