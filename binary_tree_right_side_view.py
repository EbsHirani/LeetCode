# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lowestLevel = 0
        ans = []
        def recurse(node, level):
            nonlocal lowestLevel
            if level>lowestLevel:
                lowestLevel = level
                ans.append(node.val)
            if node.right:
                recurse(node.right, level+1)
            if node.left:
                recurse(node.left, level+1)
        if root:
            recurse(root, 1)
        else:
            return []
        return ans
