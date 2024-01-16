class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n<2:return []
        ans = []
        curr = []
        def recurse(start, rem):
            if rem!=n:
                ans.append(list(curr)+[rem])
            
            for i in range(start, ceil(sqrt(rem))+1):
                if rem%i==0 and rem//i>=i:
                    # print(i, rem)
                    curr.append(i)
                    recurse(i, rem//i)
                    curr.pop()
            

        recurse(2, n)
        return ans