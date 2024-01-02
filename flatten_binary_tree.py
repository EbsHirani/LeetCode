# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def recurse(node):
            if not node:
                return None
            
            leftend = recurse(node.left)
            
            rightend = recurse(node.right)
            if leftend:
                leftend.right = node.right
                node.right = node.left
            node.left = None
            if rightend:
                return rightend
            if leftend:
                return leftend
            return node
        recurse(root)
            