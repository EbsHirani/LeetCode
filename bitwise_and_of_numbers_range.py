class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        diff = right - left
        left_b, right_b = str(bin(left))[2:], str(bin(right))[2:]
        mult = 1
        n = min(len(left_b), len(right_b))
        left_b, right_b = left_b[len(left_b)-n:], right_b[len(right_b)-n:]
        # print(left_b, right_b)
        ans = 0
        for i in range(n):
            # print(left_b[n-1-i], right_b[n-1-i], diff, mult)
            if left_b[n-1-i] == right_b[n-1-i] == '1':
                if diff<mult:
                    ans+=mult
            mult*=2
        return ans