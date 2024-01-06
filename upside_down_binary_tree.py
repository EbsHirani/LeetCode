# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        def recurse(node, parent, right):
            nonlocal ans

            nex = node.left
            nexright = node.right
            node.right = parent
            node.left = right

            if nex:
                recurse(nex, node, nexright)
            else:
                ans = node
        if not root or not root.left:
            return root
        left = root.left
        right = root.right
        root.left = None
        root.right = None
        recurse(left, root, right)
        return ans