# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def recurse(node):
            curr = str(node.val)
            ans = []
            if node.right:
                for i in recurse(node.right):
                    ans.append(curr+i)
            if node.left:
                for i in recurse(node.left):
                    ans.append(curr+i)
            if not ans:
                ans.append(curr)
            return ans
        
        rootNums = recurse(root)
        ans = 0
        for i in rootNums:
            ans+= int(i)
        return ans