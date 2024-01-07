class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        low = high = 0
        dicti = defaultdict(int)
        ans = 0
        while high<len(s):
            dicti[s[high]] +=1
            
            while len(dicti)>2:
                dicti[s[low]]-=1
                if dicti[s[low]] == 0:
                    del dicti[s[low]]
                low+=1
            
            ans = max(ans, high-low+1)
            high+=1

        return ans