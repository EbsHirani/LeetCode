# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        checked_set = set()
        start = 0
        for i in range(n):
            if i in checked_set:
                continue
            for j in range(n):
                if i==j:
                    continue
                if knows(i,j):
                    checked_set.add(i)
                    break
                if knows(j,i):
                    checked_set.add(j)
                else:
                    checked_set.add(i)
                    break
            if i not in checked_set:
                return i
        return -1
