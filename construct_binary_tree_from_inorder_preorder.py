# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recurse(preorder, inorder):
            if not preorder:
                return None
            root = TreeNode(preorder[0])
            rootval = preorder[0]
            lefti = 0
            # print(inorder, preorder)
            while inorder[lefti] != rootval:
                lefti+=1
            leftinorder = inorder[:lefti]
            rightinorder = inorder[lefti+1:]
            lefti = 0
            while lefti<len(preorder) and preorder[lefti] not in rightinorder:
                lefti+=1
            leftpreorder = preorder[1:lefti]
            rightpreorder = preorder[lefti:]
            root.left = recurse(leftpreorder, leftinorder)
            root.right = recurse(rightpreorder, rightinorder)
            return root
        
        return recurse(preorder, inorder)