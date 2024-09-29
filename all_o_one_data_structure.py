class Node:
    def __init__(self):
        self.value = None
        self.keys = set()
        self.left = None
        self.right = None


class AllOne:

    def __init__(self):
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head


    def inc(self, key: str) -> None:
        print("inserting..", key)
        if key in self.map:
            currNode = self.map[key]
            newVal = currNode.value + 1
        else:
            currNode = self.tail
            newVal = 1
        leftNode = currNode.left
        if leftNode == self.head or leftNode.value > newVal:
            newNode = Node()
            newNode.value = newVal
            newNode.right = currNode
            newNode.left = leftNode
            leftNode.right = newNode
            currNode.left = newNode
        else:
            newNode = leftNode
        if currNode!= self.tail:
            currNode.keys.remove(key)
            if len(currNode.keys) == 0:
                self.removeNode(currNode)
        newNode.keys.add(key)
        # self.print()
        self.map[key] = newNode
             

    def dec(self, key: str) -> None:
        print("decreasing..", key)
        currNode = self.map[key]
        if currNode.value == 1:
            currNode.keys.remove(key)
            if len(currNode.keys) == 0:
                self.removeNode(currNode)
            del self.map[key]
            # self.print()
            return
        rightNode = currNode.right
        newVal = currNode.value - 1
        if rightNode == self.tail or rightNode.value < newVal:
            newNode = Node()
            newNode.value = newVal
            newNode.left = currNode
            newNode.right = rightNode
            rightNode.left = newNode
            currNode.right = newNode
        else:
            newNode = rightNode
        currNode.keys.remove(key)
        if len(currNode.keys) == 0:
            self.removeNode(currNode)
        newNode.keys.add(key)
        # self.print()
        self.map[key] = newNode


    def getMaxKey(self) -> str:
        if self.head.right == self.tail:
            return ""
        return next(iter(self.head.right.keys))

    def getMinKey(self) -> str:
        if self.tail.left == self.head:
            return ""
        return next(iter(self.tail.left.keys))

    def removeNode(self, node):
        rightNode = node.right
        node.left.right = node.right
        rightNode.left = node.left

    def print(self):
        print("Printing..")
        curr = self.head.right
        while curr!=self.tail:
            print(curr.value, curr.keys)
            curr= curr.right

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()