class Solution:
    def clumsy(self, n: int) -> int:
        # 无括号的中缀表达式，遇到乘除直接算，遇到加减先入栈
        stk = []

        stk.append(n)
        n -= 1

        idx = 0

        while n:
            if idx % 4 == 0:
                stk.append(stk.pop() * n)
            elif idx % 4 == 1:
                stk.append(int(stk.pop() / n))
            elif idx % 4 == 2:
                stk.append(n)
            elif idx % 4 == 3:
                stk.append(-n)
            n -= 1
            idx += 1

        return sum(stk[:])
            