class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1000000007
        vowels = "aeiou"
        dp = {i:1 for i in vowels}
        for i in vowels:
            dp[i] = 1
        for i in range(2,n+1):
            ndp = {}
            ndp['a'] = dp['e']%MOD
            ndp['e'] = (dp['a'] + dp['i'])%MOD
            ndp['i'] = (dp['a'] + dp['e'] + dp['o'] + dp['u'])%MOD
            ndp['o'] = (dp['i'] + dp['u'])%MOD
            ndp['u'] = (dp['a'])%MOD
            dp = dict(ndp)

        ans = 0
        for i in vowels:
            ans+= dp[i]
        return ans%MOD