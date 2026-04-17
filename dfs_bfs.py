
# DFS/BFS Pattern (Tree Traversal Example)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def dfs_preorder(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

from collections import deque

def bfs_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Example usage:
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# print(dfs_preorder(root)) # Output: [1, 2, 4, 5, 3]
# print(bfs_level_order(root)) # Output: [1, 2, 3, 4, 5]
