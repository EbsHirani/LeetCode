class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab_lcm = math.lcm(a,b)
        bc_lcm = math.lcm(b,c)
        ac_lcm = math.lcm(a,c)
        abc_lcm = math.lcm(a,b,c)

        def ugly_count(num):
            return num//a + num//b + num//c - num//ab_lcm - num//bc_lcm - num//ac_lcm + num//abc_lcm
        
        low = 0
        high = min(a,b,c)*n
        ans = high
        while high >= low:
            mid = (high+low)//2
            # print(ans)
            if ugly_count(mid) >= n:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans