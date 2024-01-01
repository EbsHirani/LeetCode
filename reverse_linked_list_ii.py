# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        if left == right or not head or not head.next:
            return head
        curr = head

        while count<left-1:
            curr = curr.next
            count+=1
        leftStart = curr
        if left!=1:
            leftNode = leftStart.next
        else:
            leftNode=leftStart
        while count<right:
            curr = curr.next
            count+=1
        rightNode = curr
        rightEnd = curr.next
        prev = leftNode
        curr = prev.next
        while curr!=rightNode:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr=temp
        rightNode.next = prev
        leftNode.next = rightEnd
        if left ==1:
            return rightNode
        leftStart.next = rightNode
        
        
        return head

###One Pass Solution
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        if left == right or not head or not head.next:
            return head
        curr = head

        while count<left-1:
            curr = curr.next
            count+=1
        leftStart = curr
        if left!=1:
            leftNode = leftStart.next
        else:
            leftNode=leftStart
        prev = leftNode
        while count<right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr=temp
            count+=1
        rightNode = curr
        rightEnd = curr.next
        rightNode.next = prev
        leftNode.next = rightEnd
        if left ==1:
            return rightNode
        leftStart.next = rightNode
        
        
        return head





