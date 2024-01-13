class Solution:
    def calculate(self, s: str) -> int:
        
        prev_num = 0
        total = 0
        currNum=""
        op = '+'
        for id, i in enumerate(s):
            # print(stack)
            # print(i, op)
            if i.isdigit():
                currNum+=i
            if i in "+-/*" or id==len(s)-1:
                # print(op, "op")
                if op == "+":
                    total += prev_num
                    prev_num = int(currNum)
                elif op == "-":
                    total += prev_num
                    prev_num = -int(currNum)
                elif op == "*":
                    prev_num = prev_num * int(currNum)
                    # print(prev_num)
                    
                elif op == "/":
                    prev_num = prev_num / int(currNum)
                    if prev_num < 0:
                        prev_num = ceil(prev_num)
                    else:
                        prev_num = floor(prev_num)
                op = i
                currNum = ""

        return total + prev_num