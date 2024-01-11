class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [1]*(n)
        ans = 0
        for i in range(2, floor(sqrt(n))+1):
            if arr[i] == 1:
                ans+=1
                start = i
                while i*start<n:
                    arr[i*start] = -1
                    start+=1
        
        for i in range(floor(sqrt(n))+1, len(arr)):
            if arr[i] == 1:
                ans+=1
        # print(arr)
        return ans