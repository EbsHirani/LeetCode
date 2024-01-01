class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        visited = set(ans)
        mult = [1]
        for i in range(1, n):
            mult.append(mult[-1]*2)

        arr = [0]*n 

        def recurse(num):   
            for i in range(n):
                if arr[i] == 0:
                    temp = num + mult[i]
                    if temp not in visited:
                        arr[i] = 1
                        ans.append(temp)
                        visited.add(temp)
                        recurse(temp)
                        return
                else:
                    temp = num - mult[i]
                    if temp not in visited:
                        arr[i] = 0
                        ans.append(temp)
                        visited.add(temp)
                        recurse(temp)
                        return
        recurse(0)
        return ans