# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        mini = float("inf")
        mininode = None
        def recurse(node):
            nonlocal mini, mininode
            if not node:
                return
            if node.val>p.val and node.val < mini:
                mini = node.val
                mininode = node
            recurse(node.left)
            recurse(node.right)
        recurse(root)
        if mini!=float("inf"):
            return mininode
        return None
            
