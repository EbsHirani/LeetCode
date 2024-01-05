# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Find Mid

        slow = fast = head
        prev = None
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        
        if fast == slow or slow.next == fast:
            return
        curr = slow.next
        slow.next = None

        #reverse
        prev = None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            
        curr2 = prev
        curr = head

        #merge
        while curr2 and curr:
            nex, nex2 = curr.next, curr2.next

            curr2.next = nex
            curr.next = curr2

            curr,curr2 = nex, nex2