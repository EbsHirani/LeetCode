class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for num in range(1,numRows+1):
            li = [1]*num
            for i in range(1,num-1):
                li[i] = ans[-1][i-1] + ans[-1][i]
            ans.append(li)
        return ans
