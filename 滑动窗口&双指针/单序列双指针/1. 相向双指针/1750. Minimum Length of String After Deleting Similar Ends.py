class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i, j = 0, n - 1

        while i < j: # 不带等号，因为i == j时只有一个元素, 不能消除
            if s[i] == s[j]:
                ch = s[i]
                while i <= j and s[i] == ch: # 带等号，因为i == j - 1时, 有不止一个元素，可消除
                    i += 1

                while i <= j and s[j] == ch:
                    j -= 1
            else:
                break
        return j - i + 1