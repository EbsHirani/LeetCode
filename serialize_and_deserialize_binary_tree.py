# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans =""
        def dfs(node):
            nonlocal ans
            if not node:
                ans+= "None,"
            else:
                # print(node.val)
                ans+=str(node.val) + ","
                dfs(node.left)
                dfs(node.right)
            
        # print(ans)
        dfs(root)
        # print(ans)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # print("str:", data)
        li = data.split(",")
        # print(li)
        def dfs(index):
            if li[index] == "None" or li[index] == "":
                return None, index
            else:
                node = TreeNode(int(li[index]))
                left, end = dfs(index+1)
                right, end = dfs(end+1)
                node.left = left
                node.right = right
                return node, end

        ans, _ = dfs(0)
        return ans
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))