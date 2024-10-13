class Solution:
    def calculate(self, s: str) -> int:
        # first, infix expression -> postfix expression
        # then, calculate postfix expression

        s = s.replace(' ', "")

        def infix_to_postfix(s):
            op_stk = []
            res = []

            # 定义操作符的优先级
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

            i = 0
            while i < len(s):
                ch = s[i]

                # 处理数字（包括负数）
                if '0' <= ch <= '9':
                    num = ''
                    while i < len(s) and '0' <= s[i] <= '9':
                        num += s[i]
                        i += 1
                    res.append(num)
                    continue

                # 处理负号：当负号位于表达式开头或在左括号之后时，作为0减某数处理
                # 如：-(-5+10) => 0-(0-5+10);
                elif ch == '-' and (i == 0 or s[i - 1] == '('):
                    res.append('0')
                    op_stk.append('-')

                # 处理左括号
                elif ch == '(':
                    op_stk.append(ch)

                # 处理右括号
                elif ch == ')':
                    while op_stk and op_stk[-1] != '(':
                        res.append(op_stk.pop())
                    if op_stk:
                        op_stk.pop()  # 弹出'('

                # 处理操作符
                else:
                    while (op_stk and op_stk[-1] != '(' and
                        precedence.get(op_stk[-1], 0) >= precedence.get(ch, 0)):
                        res.append(op_stk.pop())
                    op_stk.append(ch)

                i += 1

            # 处理栈中剩余的操作符
            while op_stk:
                res.append(op_stk.pop())

            return res

        postfix_exp = infix_to_postfix(s)
        print(postfix_exp)
        
        # 计算后缀表达式
        stk = []
        ans = 0
        for token in postfix_exp:
            if token in ('+', '-', '*', '/'):
                b = int(stk.pop())
                a = int(stk.pop())
                if token == '+':
                    stk.append(a + b)
                elif token == '-':
                    stk.append(a - b)
                elif token == '*':
                    stk.append(a * b)
                elif token == '/':
                    stk.append(int (a / b))
            else:
                stk.append(token)

        return int(stk[-1])