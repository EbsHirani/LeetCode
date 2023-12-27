class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            ans=1
            for i in range(1,n+1):
                ans*=i
            return ans
        
        arr = list(range(1,n+1))
        ans = ""
        while arr:
            n = len(arr)
            fact = factorial(n-1)
            temp = 1
            while k>temp*fact:
                temp+=1
            id = temp-1
            ans += str(arr.pop(id))
            k-=(temp-1)*fact
        
        return ans