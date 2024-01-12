class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = set()
        rot = ((0,1), (1,0), (0,-1), (-1,0))
        ans = []
        def recurse(node,x,y, curr):
            if node.is_end and curr not in ans:
                # print(x,y, curr)
                ans.append(str(curr))
            visited.add((x,y))
            for i,j in rot:
                if 0<=x+i<len(board) and 0<=y+j<len(board[0]):
                    if (x+i,y+j) not in visited and board[x+i][y+j] in node.children:
                        
                        recurse(node.children[board[x+i][y+j]], x+i, y+j, curr+board[x+i][y+j])
            visited.remove((x,y))
            return False
        
        root = TrieNode()

        for word in words:
            curr = root
            
            for c in word:
                if c not in curr.children:
                    newNode = TrieNode()
                    curr.children[c] = newNode
                curr = curr.children[c]
            curr.is_end = True

        for x in range(len(board)):
            for y in range(len(board[0])):
                # print("start",x,y)
                if board[x][y] in root.children:
                    recurse(root.children[board[x][y]], x,y,board[x][y])
        return ans