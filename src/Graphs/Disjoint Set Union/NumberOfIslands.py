# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: