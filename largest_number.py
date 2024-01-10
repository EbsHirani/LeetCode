class LargerNumKey(str):
    def __lt__(x, y):
        return x+y < y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = sorted(list(map(str, nums)), key = LargerNumKey, reverse = True)
        
        ans = "".join(nums)
        i = 0
        while i<len(ans) and ans[i] == '0':
            i+=1
        print(i)
        if i == len(ans):
            return '0'
        
        return ans[i:]