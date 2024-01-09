# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        parent = None
        node = root
        self.stack = []
        while node:
            self.stack.append(node)
            node = node.left

        

    def next(self) -> int:
        if self.stack:
            ans = self.stack.pop()
            if ans.right:
                node = ans.right
                while node:
                    self.stack.append(node)
                    node = node.left
            return ans.val
        return None
        

    def hasNext(self) -> bool:
        return len(self.stack)>0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()