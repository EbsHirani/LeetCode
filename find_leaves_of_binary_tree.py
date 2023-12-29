# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs(node):
            if not node.left and not node.right:
                return True
            
            if node.left and dfs(node.left):
                ans.append(node.left.val)
                node.left = None
            
            if node.right and dfs(node.right):
                ans.append(node.right.val)
                node.right = None

            return False
            
        final = []
        while root.left or root.right:
            dfs(root)
            final.append(list(ans))
            ans = []
        
        final.append([root.val])
        
        return final
        


#ALT
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        dicti = defaultdict(list)

        def dfs(node):
            if not node.left and not node.right:
                dicti[0].append(node.val)
                return 0
            
            ht = 0
            if node.left:
                ht = dfs(node.left) + 1
            
            if node.right:
                ht = max(ht, dfs(node.right) + 1)
            dicti[ht].append(node.val)
            return ht
            
        dfs(root)

        ans = [[] for _ in range(max(dicti.keys())+1)]
        for i in range(len(ans)):
            ans[i] = dicti[i]

        return ans
        
