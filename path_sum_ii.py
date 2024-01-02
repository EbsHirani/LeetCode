# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        curr = []
        if not root:
            return []
        def recurse(total, node):
            
            if total+node.val == targetSum and node.left==node.right==None:
                ans.append(curr + [node.val])
                return
            curr.append(node.val)
            if node.left:
                recurse(total+node.val, node.left)
            if node.right:
                recurse(total+node.val, node.right)
            curr.pop()
        recurse(0, root)
        return ans