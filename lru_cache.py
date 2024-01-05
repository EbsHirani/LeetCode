class Node:
    def __init__(self, key, val, prev = None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.currSize =  0
        self.capacity = capacity
        self.tail = None
        self.head = None
        self.fromKeyToLi = {}

    def make_node_first(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail = self.tail.prev
        if node.prev: node.prev.next = node.next
        if node.next: node.next.prev = node.prev
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node
        # print(self.head.val, self.tail.val)


    def get(self, key: int) -> int:
        if key in self.fromKeyToLi:
            node = self.fromKeyToLi[key]
            self.make_node_first(node)
            return self.fromKeyToLi[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.fromKeyToLi:
            node = self.fromKeyToLi[key]
            node.val = value
            self.make_node_first(node)
        else:
            node = Node(key, value)
            node.next = self.head
            if self.currSize == 1:
                self.tail = self.head
            if self.head: self.head.prev = node
            self.head = node
            self.fromKeyToLi[key] = node
            print("head:", self.head.key)
            if self.tail: print("tail:", self.tail.key)
            if self.currSize == self.capacity:
                # print("del time", key, self.tail.val)
                del self.fromKeyToLi[self.tail.key]
                self.tail = self.tail.prev
                print("tail:", self.tail.key)
                self.tail.next = None
            else:
                self.currSize+=1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)