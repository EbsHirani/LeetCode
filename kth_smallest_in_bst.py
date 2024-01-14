# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        def recurse(node, onleft):
            nonlocal ans
            if not node:
                return 0
            onleft += max(recurse(node.left, onleft) - onleft, 0)
            print(node.val, onleft)
            if onleft == k-1:
                ans = node.val
            onleft+=1
            if onleft<k:
                onleft += max(recurse(node.right, onleft)-onleft, 0)
            return onleft
        recurse(root, 0)
        return ans if ans else 0