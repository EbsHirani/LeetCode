class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for i in s:
            if i.isdigit():
                size = size*int(i)
            else:
                size+=1
        for i in reversed(s):
            if not i.isdigit():
                if k == size or k==0:
                    return i
                size -= 1
            else:
                size = size//int(i)
                k%=size