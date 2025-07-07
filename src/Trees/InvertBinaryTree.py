from collections import deque

# DFS Solution
def invertTree(self, root):
    if not root:
        return None
    
    # actual inversion here
    temp = root.right
    root.right = root.left
    root.left = temp

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root

# BFS Solution
def invertTree(self, root):
    if not root:
        return None
    q = deque([root])
    while q:
        curr = q.popleft()

        temp = curr.left
        curr.left = curr.right
        curr.right = temp

        if (curr.left):
            q.append(curr.left)
        if (curr.right):
            q.append(curr.right)
    return root


