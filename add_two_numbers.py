# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        val = l1.val+l2.val
        carry = 0
        if val >=10:
            carry = val//10
            val = val%10
        head = ListNode(val)
        curr = head
        l1 = l1.next
        l2 = l2.next

        while l1 or l2:
            prev = curr

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            carry = 0
            if val >=10:
                carry = val//10
                val = val%10
            curr = ListNode(val)
            prev.next = curr
            if l1:
                l1 = l1.next
            if l2:                
                l2 = l2.next
        if carry!=0:
            curr.next = ListNode(carry)
        
        return head

