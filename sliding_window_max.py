class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = right = 0
        dq = deque()
        ans = []
        while right < len(nums):
            if right == 25:
                print()
            while dq and dq[-1]<nums[right]:
                dq.pop()
            dq.append(nums[right])
            if right-left+1 > k:
                if nums[left] == dq[0]:
                    dq.popleft()
                left+=1
            if right-left+1 == k:
                ans.append(dq[0])
            right+=1
        return ans