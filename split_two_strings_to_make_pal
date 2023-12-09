class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if a == a[::-1] or b == b[::-1]:
            return True
        
        for i in range(len(a)//2 +1):
            print(a[i], b[len(b)- i - 1])
            if a[i] != b[len(b)- i - 1]:
                break
        

        a_end = i-1
        b_start = len(b) - i

        for i in range(len(a)//2 +1):
            # print(b[i], a[len(b)- i - 1])
            if b[i] != a[len(a)- i - 1]:
                break
        b_end = i-1
        a_start = len(a) - i 
        def isPal(s):
            return s == s[::-1]
        
        return isPal(a[:b_start] + b[b_start:]) or isPal(a[:a_end+1] + b[a_end+1:]) or isPal(b[:b_end+1] + a[b_end+1:]) or isPal(b[:a_start] + a[a_start:])
