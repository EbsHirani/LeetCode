# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        newhead = None
        curr = head
        i = 0
        while curr:
            nex = curr.next
            curr.next = None
            if not newhead:
                newhead = curr
            
            else:
                if curr.val<=newhead.val:
                    curr.next = newhead
                    newhead = curr
                else:
                    newcurr = newhead
                    while newcurr.next:
                        if curr.val <= newcurr.next.val:
                            curr.next = newcurr.next
                            newcurr.next=curr
                            break
                        
                        newcurr = newcurr.next
                    if curr.val > newcurr.val:
                        newcurr.next = curr
            
            curr = nex
            
        return newhead

            