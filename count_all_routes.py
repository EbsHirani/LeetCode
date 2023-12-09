class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = [[-1] * (fuel+1) for _ in range(len(locations))] 
        def recurse(loc, fuel):
            
            if dp[loc][fuel] != -1:
                return dp[loc][fuel]
            ans = 0
            if loc == finish:
                ans = 1
            for i in range(len(locations)):
                if i != loc and abs(locations[i]-locations[loc]) <= fuel:
                    ans += recurse(i, fuel - abs(locations[i]-locations[loc]))%(1000000007)
            dp[loc][fuel] = ans%(1000000007)
            return dp[loc][fuel]
        
        return recurse(start, fuel)
