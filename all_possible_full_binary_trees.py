# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2 == 0:
            return []
        dp = [None]*(n+1)
        def explore(n):
            if n==1:
                return [TreeNode(0)]
            if dp[n] != None:
                return dp[n]
            ans = []
            for i in range(1,n-1,2):
                lefts = explore(i)
                rights = explore(n-1-i)
                for left in lefts:
                    for right in rights:
                        ans.append(TreeNode(0,left,right))
            dp[n] = ans
            return ans
        return explore(n)

            