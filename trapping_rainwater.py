class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):

            while stack and height[stack[-1]]<height[i]:
                st = stack.pop()
                if stack:
                    stleft = stack[-1]
                    ht = min(height[stleft], height[i]) - height[st]
                    dist = i - stleft -1
                    ans += dist*ht
            stack.append(i)
        return ans