# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = float("-inf")
        
        def recurse(node):
            nonlocal ans
            
            leftSum=0
            rightSum = 0
            if node.left:
                leftSum = max(leftSum, recurse(node.left))
            if node.right:
                rightSum = max(rightSum, recurse(node.right))
            tempAns = max(node.val + leftSum + rightSum, node.val+leftSum, node.val + rightSum, node.val)
            ans = max(ans, tempAns)

            return max(node.val+leftSum, node.val + rightSum, node.val)
        
        recurse(root)
        return ans

            