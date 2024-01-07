# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergesort(head):
            if not head or not head.next:
                return head
            slow = fast = head
            prev= None
            while fast:
                fast = fast.next
                if fast:
                    prev= slow
                    slow = slow.next
                    fast= fast.next
            prev.next = None
            firstList = mergesort(head)
            secondList = mergesort(slow)
            curr1, curr2 = firstList, secondList
            new = None
            newHead = None
            while curr1 and curr2:
                if curr1.val < curr2.val:
                    temp= curr1.next
                    curr1.next = None
                    if new:
                        new.next = curr1
                        new = new.next
                    else:
                        new = curr1
                        newHead = new
                    curr1 = temp
                else:
                    temp= curr2.next
                    curr2.next = None
                    if new:
                        new.next = curr2
                        new = new.next
                    else:
                        new = curr2
                        newHead = new
                    curr2 = temp
            if curr1:
                new.next = curr1
            elif curr2:
                new.next = curr2
            return newHead
        return mergesort(head)