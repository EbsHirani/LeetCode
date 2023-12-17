class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 1000000007
        dp = [-1]*len(s)
        def recurse(i):
            if i<0:
                return 1
            if dp[i]!=-1:
                return dp[i]
            ans = 0
            if s[i] == "*":
                ans = ans + 9*recurse(i-1)%MOD
                if i>0 and s[i-1] == "1":
                    ans = ans + 9*recurse(i-2)%MOD
                elif i>0 and s[i-1] == "2":
                    ans = ans + 6*recurse(i-2)%MOD
                elif i>0 and s[i-1] == "*":
                    ans = ans + 15*recurse(i-2)%MOD
            else:
                if s[i]!="0":
                    ans+=recurse(i-1)
                if i>0 and s[i-1] == "1":
                    ans = ans + recurse(i-2)%MOD
                elif i>0 and int(s[i])<7 and s[i-1] == "2":
                    ans = ans + recurse(i-2)%MOD
                elif i>0 and s[i-1] == "*":
                    if int(s[i])<7:
                        ans = ans + 2*recurse(i-2)%MOD
                    else:
                        ans = ans + recurse(i-2)%MOD
            dp[i] = ans%MOD
            return dp[i]

        return recurse(len(s)-1)
        