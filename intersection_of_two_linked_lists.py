# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curr = headA
        n = 0
        while curr:
            curr= curr.next
            n+=1        
        m = 0
        curr = headB
        while curr:
            curr= curr.next
            m+=1
        
        i = 0
        curr = headB
        while i<m-n:
            curr = curr.next
            i+=1

        startB = curr
        curr = headA
        while i<n-m:
            curr = curr.next
            i+=1
        startA = curr

        while startA!=startB:
            startA = startA.next
            startB = startB.next
        
        return startA
        