class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        right = 0
        dicti = defaultdict(int)
        k_count = 0
        ans = float("-inf")
        while right<len(s):
            c = s[right]
            dicti[c]+=1
            if dicti[c]==1:
                k_count+=1
            # print(c, dicti)
            while left<=right and k_count>k:
                c1 = s[left]
                dicti[c1]-=1
                if dicti[c1] == 0:
                    k_count-=1
                left+=1
            ans = max(ans, right-left+1)
            # print(s[left:right+1], k_count, dicti)
            right+=1
        return ans