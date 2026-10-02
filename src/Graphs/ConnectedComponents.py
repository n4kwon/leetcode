# You have an undirected graph of n nodes labeled from 0 to n - 1. 
# You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge 
# between aᵢ and bᵢ in the graph. Return the number of connected components in the graph.

# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

from collections import defaultdict, deque

class Solution:
    # DFS
    def numberOfComponents(n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited = [False] * n
        def dfs(curr):
            for neighbour in adj[curr]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)

        components = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                components += 1
        return components



    # BFS
    def numberOfComponents(n: int, edges: list[list[int]]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited = set()
        def bfs(curr):
            q = deque()
            q.append(curr)
            while q:
                node = q.popleft()
                for neighbour in adj[node]:
                    if neighbour in visited:
                        continue
                    visited.add(neighbour)
                    q.append(neighbour)

        components = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                bfs(i)
                components += 1
        return components