# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        fromLeft = True
        queue = deque()
        queue.append((root,0))
        while queue:
            nextLevel = deque()
            temp = []
            while queue:
                if fromLeft:
                    node, level = queue.popleft()
                    if node.left:
                        nextLevel.append((node.left, level+1))
                    if node.right:
                        nextLevel.append((node.right, level+1))
                else:
                    node, level = queue.pop()
                    if node.right:
                        nextLevel.appendleft((node.right, level+1))
                    if node.left:
                        nextLevel.appendleft((node.left, level+1))
                temp.append(node.val)
            ans.append(temp)
            queue = nextLevel
            fromLeft = not fromLeft
        return ans