class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+*-/":
                op2 = stack.pop()
                op1 = stack.pop()                
                if i == '+':
                    stack.append(op1+op2)
                elif i == '-':
                    stack.append(op1-op2)
                elif i == '*':
                    stack.append(op1*op2)
                else:
                    temp = op1/op2
                    if temp >0:
                        stack.append(floor(temp))
                    else:
                        stack.append(ceil(temp))
            else:
                stack.append(int(i))
        
        return stack.pop()