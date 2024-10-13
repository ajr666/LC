class Solution:
    def clearStars(self, s: str) -> str:
        # delete the smallest, and the rightest element in s

        stacks = [[] for _ in range(26)] # 26 stacks, every time delete the first non-empty stack's top
        to_delete = set()

        for i, c in enumerate(s):
            if c != '*':
                stacks[ord(c) - ord('a')].append(i)
            else:
                for stk in stacks:
                    if stk:
                        to_delete.add(stk.pop())
                        break
        
        ans = ''
        for i in range(len(s)):
            if s[i] != '*' and i not in to_delete:
                ans += s[i]
        return ans