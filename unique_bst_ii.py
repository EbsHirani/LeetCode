# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[None]*(n+1) for _ in range(n+1)]

        def recurse(start, end):
            if start == end:
                return [TreeNode(start)]
            if start>end:
                return [None]
            elif dp[start][end]:
                return dp[start][end]
            ans = []
            for i in range(start,end+1):
                leftSet = recurse(start, i-1)
                rightSet = recurse(i+1, end)
                for left in leftSet:
                    for right in rightSet:
                        ans.append(TreeNode(i, left, right))
            dp[start][end] = ans
            return ans
        
        return recurse(1, n)