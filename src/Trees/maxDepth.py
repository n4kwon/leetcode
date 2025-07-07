# DFS implementation
from collections import deque


def maxDepth(self, root) -> int:
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# BFS implementation
def maxDepth(self, root) -> int:
    q = deque([root])
    depth = 0
    while q:
        for i in range(len(q)):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        depth += 1
    return depth
