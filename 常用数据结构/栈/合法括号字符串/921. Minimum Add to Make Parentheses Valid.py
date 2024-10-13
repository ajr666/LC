class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        
        for ch in s:
            if stk and stk[-1] == '(' and ch == ')':
                stk.pop()
            else:
                stk.append(ch)

        return len(stk)