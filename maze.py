import queue
from collections import deque


class MazeSolver:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.move_x = [-1, 0, 0, 1]
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for i in range(self.n)] for j in range(self.n)]
        self.min_distance = float('inf')

    def is_valid(self, row, col):
        if row < 0 or row >= self.n:
            return False
        if col < 0 or col >= self.n:
            return False
        if self.matrix[row][col] == 0:
            return False

        if self.visited[row][col]:
            return False

        return True

    def search(self, start_x, start_y, end_x, end_y):
        queue = deque()
        queue.append((start_x, start_y, 0))
        while queue:
            (curr_x, curr_y, distance) = queue.popleft()
            for i in range(4):
                next_x = curr_x + self.move_x[i]
                next_y = curr_y + self.move_y[i]
                if self.is_valid(next_x, next_y):
                    queue.append((next_x, next_y, distance + 1))
                    self.visited[next_x][next_y] = True
                    if next_x == end_x and next_y == end_y:
                        self.min_distance = min(distance + 1, self.min_distance)

    def show_result(self):
        return self.min_distance


if __name__ == '__main__':
    m = [
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    solver = MazeSolver(m)
    solver.search(0, 0, 4, 4)
    print(solver.show_result())
