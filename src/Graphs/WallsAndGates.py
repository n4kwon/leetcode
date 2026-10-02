# You are given a m×n 2D grid initialized with these three possible values:

# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest 
# then the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        visited = set()
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx = row + dx
                    ny = col + dy
                    if nx < 0 or nx >= len(grid):
                        continue
                    if ny < 0 or ny >= len(grid[0]):
                        continue
                    if grid[nx][ny] == -1 or (nx, ny) in visited:
                        continue
                    q.append((nx, ny))
                    visited.add((nx, ny))
            dist += 1
                    


























from collections import deque
from typing import List

# Backtracking with DFS
# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         INF = 2147483647
#         visited = set()
#         def dfs(x, y):
#             if x < 0 or x >= len(grid):
#                 return INF
#             if y < 0 or y >= len(grid[0]):
#                 return INF
#             if grid[x][y] == 0:
#                 return 0
#             if grid[x][y] == -1 or (x, y) in visited:
#                 return INF
            
#             visited.add((x, y))
#             res = INF
#             for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 res = min(res, 1 + dfs(x + dx, y + dy))
#             visited.remove((x, y))
#             return res

#         for r in range(len(grid)):
#             for c in range(len(grid)):
#                 if grid[r][c] == INF:
#                   grid[r][c] = dfs(r, c)


# BFS
# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         INF = 2147483647
#         def bfs(x, y):
#             q = deque([x, y])
#             visited = [[False] * len(grid) for _ in range(grid[0])]
#             step = 0
#             while q:
#                 for _ in range(len(q)):
#                     r, c = q.popleft()
#                     if grid[r][c] == 0:
#                         return step
#                     for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                         nx = dx + r
#                         ny = dy + c
#                         if 0 <= nx <= len(grid) and 0 <= ny <= len(grid[0]) and grid[nx][ny] != -1 and not visited[nx][ny]:
#                             visited[nx][ny] = True
#                             q.append((nx, ny))
#                 step += 1
#             return INF
        
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == INF:
#                     grid[r][c] = bfs(r, c)

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        visited = set()
        q = deque()

        def addCells(x, y):
            if x < 0 or x >= len(grid):
                return
            if y < 0 or y >= len(grid):
                return
            if grid[x][y] == -1 or (x, y) in visited:
                return

            q.append([x, y])
            visited.add((x, y))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    addCells(r, c)

        steps = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = steps
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    addCells(row + dx, col + dy)
            steps += 1
                    