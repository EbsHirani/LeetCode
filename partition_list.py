# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        leftHead = rightHead = None
        if head.val<x:
            leftHead = head
        else:
            rightHead = head
        leftcurr = leftHead
        rightcurr = rightHead

        curr = head.next
        head.next = None
        while curr:
            nex = curr.next
            curr.next = None
            if curr.val<x:
                if leftcurr:
                    leftcurr.next = curr
                    leftcurr = curr
                else:
                    leftHead = leftcurr = curr
            else:
                if rightcurr:
                    rightcurr.next = curr
                    rightcurr = curr
                else:
                    rightHead = rightcurr = curr
            curr = nex
        
        if not leftHead:
            return rightHead
        if not rightHead:
            return leftHead
        leftcurr.next = rightHead
        return leftHead