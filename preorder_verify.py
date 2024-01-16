class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        left = 0
        stack = [preorder[0]]
        for i in range(1, len(preorder)):
            if preorder[i]<left:
                return False
            while stack and stack[-1]<preorder[i]:
                left = stack.pop()
            stack.append(preorder[i])
        return True