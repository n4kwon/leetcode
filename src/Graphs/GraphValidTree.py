# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to check whether these edges make up a valid tree.


# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

# Definition of a Tree:
# Connected, no cycles, n - 1 edges for n nodes

from collections import defaultdict, deque

class Solution:
    def graph_valid_tree(n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        visited = set()
        def dfs(curr, parent):
            if curr in visited:
                return False
            visited.add(curr)
            for neighbour in adj[curr]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, curr):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n







        
    # def graph_valid_tree(n: int, edges: list[list[int]]) -> bool:
    #     if len(edges) != n - 1:
    #         return False
    #     adj = defaultdict(list)
    #     for v1, v2 in edges:
    #         adj[v1].append(v2)
    #         adj[v2].append(v1)

    #     q = deque()
    #     q.append(0, -1)
    #     visited = set()
    #     visited.add(0)
    #     while q:
    #         node, parent = q.popleft()
    #         for neighbour in adj[node]:
    #             if neighbour == parent:
    #                 continue
    #             if neighbour in visited:
    #                 return False
    #             visited.add(neighbour)
    #             q.append(neighbour, node)

    #     return len(visited) == n
    





        
            
