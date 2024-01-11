class Node:
    def __init__(self, isEnd = False):
        self.children = {}
        self.isEnd = isEnd
class Trie:

    def __init__(self):
        self.root = Node()        

    def insert(self, word: str) -> None:
        i = 0
        node = self.root
        
        while i<len(word) and word[i] in node.children:
            node = node.children[word[i]]
            i+=1
        parent = node
        while i<len(word):
            temp = Node()
            parent.children[word[i]] = temp
            i+=1
            parent = temp
        parent.isEnd = True
    def search(self, word: str) -> bool:
        i = 0
        node = self.root
        while i<len(word):
            if word[i] not in node.children:
                return False
            node = node.children[word[i]]
            i+=1
        return node.isEnd
            


    def startsWith(self, prefix: str) -> bool:
        i = 0
        node = self.root
        while i<len(prefix):
            print(node.children)
            if prefix[i] not in node.children:
                return False
            node = node.children[prefix[i]]   
            i+=1
        return True   


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)