# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findMid(node):
            slow = node
            prev = slow
            while node != None:
                node = node.next
                if node:
                    prev = slow
                    node = node.next
                    slow = slow.next
            return slow, prev
        
        def recurse(node):
            if not node:
                return None
            mid, prev_mid = findMid(node)
            tnode = TreeNode(mid.val)
            if mid == node:
                return tnode
            left = right = None
            if prev_mid!=mid:
                prev_mid.next = None
                left =recurse(node)
            
            right = recurse(mid.next)
            tnode.left, tnode.right = left, right
            return tnode
        
        return recurse(head)

        return None