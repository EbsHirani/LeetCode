# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def recurse(node):
            nonlocal ans
            if not node:
                return False, False
            hasp = hasq = False
            if node == p:
                hasp = True
                # print("foundp".)
            if node == q:
                hasq = True
                # print("foundq")
            # print(hasp, hasq, node.val)
            tempp, tempq = recurse(node.left)
            hasp = hasp or tempp
            hasq = hasq or tempq
            tempp, tempq = recurse(node.right)
            hasp = hasp or tempp
            hasq = hasq or tempq
            # print(hasp, hasq, node.val)
            if hasp and hasq and not ans:
                ans = node
            return hasp, hasq
        
        recurse(root)
        return ans
            
            
        