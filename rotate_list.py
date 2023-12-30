# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        curr = head
        n = 0

        while curr:
            n+=1
            curr = curr.next
        if n<=1 or k%n==0:
            return head
        
        k = k%n

        newHeadDist = n-k-1
        curr = head
        while newHeadDist:
            curr = curr.next
            newHeadDist-=1
        
        endNode = newHead = curr.next
        curr.next = None

        while endNode.next:
            endNode = endNode.next
        
        endNode.next = head

        return newHead
        

        