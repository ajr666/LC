class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if token == '+':
                b = stk.pop()
                a = stk.pop()
                stk.append(a + b)

            elif token == '-':
                b = stk.pop()
                a = stk.pop()
                stk.append(a - b)

            elif token == '*':
                b = stk.pop()
                a = stk.pop()
                stk.append(a * b)
            
            elif token == '/':
                b = stk.pop()
                a = stk.pop()
                stk.append(int(a / b))

            else:
                num = int(token)
                stk.append(num)
        
        return stk[-1]