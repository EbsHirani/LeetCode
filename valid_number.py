class Solution:
    def isNumber(self, s: str) -> bool:
        state = "before."
        if s[0] == '+' or s[0] =='-':
            s= s[1:]
        if len(s)==0:
            return False
        i = 0
        while i<len(s):
            if state == "before.":
                if not s[i].isdigit():
                    if s[i] == "." and len(s)!= 1:
                        state = "after."
                    elif s[i].lower() == 'e' and i+1 < len(s) and i!=0 and (s[i-1].isdigit() or ((i-2)>=0 and s[i-2].isdigit())):
                        if s[i+1] == "+" or s[i+1] == '-':
                            i+=1
                            if i+1>=len(s):
                                return False
                        state = "aftere"
                    else:
                        return False
            elif state == "after.":
                if not s[i].isdigit():
                    if s[i].lower() == 'e' and i+1 < len(s) and i!=0 and (s[i-1].isdigit() or ((i-2)>=0 and s[i-2].isdigit())):
                        if s[i+1] == "+" or s[i+1] == '-':
                            i+=1
                            if i+1>=len(s):
                                return False
                        state = "aftere"
                    else:
                        return False
            elif state == "aftere":
                if not s[i].isdigit():
                    return False
            i+=1
        return True
