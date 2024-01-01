# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postId = len(postorder) - 1
        inorder_hash = {inorder[i]:i for i in range(len(inorder))}
        def recurse(left, right):
            nonlocal postId
            if right<left:
                return None
            rootval = postorder[postId]
            root = TreeNode(rootval)
            postId-=1
            leftend = inorder_hash[rootval]-1
            rightstart = inorder_hash[rootval]+1
            root.right = recurse(rightstart,right)
            root.left = recurse(left, leftend)
            return root
        
        return recurse(0,len(postorder)-1)
