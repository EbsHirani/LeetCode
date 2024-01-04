"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        pointer_map = {}
        newHead = Node(head.val)
        pointer_map[head] = newHead

        prevNew = newHead
        currOld = head.next
        while currOld:
            
            new = Node(currOld.val)
            pointer_map[currOld] = new
            prevNew.next = new

            prevNew = prevNew.next
            currOld = currOld.next
        
        currOld = head
        while currOld:
            currNew = pointer_map[currOld]
            if currOld.random:
                currNew.random = pointer_map[currOld.random]
                print(currNew.val, currOld.val, currOld.random.val)
            currOld= currOld.next
        return newHead