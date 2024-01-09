class Solution:
    def trailingZeroes(self, n: int) -> int:
        pow = 1
        div = 5
        while n//div != 0:
            div*=5
            pow+=1
        ans = 0
        for i in reversed(range(1,pow+1)):
            # print(i, div, n)
            ans += (n//div)
            div = div//5
            print(ans)
        return ans 