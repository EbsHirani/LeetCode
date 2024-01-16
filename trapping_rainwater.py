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

#2 pointer solution
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height)-1
        leftmax = rightmax = 0

        while left<right:
            if height[left]< height[right]:
                if height[left]<leftmax:
                    ans+= leftmax-height[left]
                else:
                    leftmax = height[left]
                left+=1
            else:
                if height[right]<rightmax:
                    ans+= rightmax - height[right]
                else:
                    rightmax = height[right]
                right-=1
        return ans
                    

        return ans