class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)

        ans = 0

        for i in range(26): # first enumerate both, then middle
            c = chr(ord('a') + i)

            l = 0
            r = n - 1

            while l < n and s[l] != c:
                l += 1

            while r >= 0 and s[r] != c:
                r -= 1

            if l + 2 > r:
                continue

            st = set()
            for k in range(l + 1, r):
                st.add(s[k])
            ans += len(st)

        return ans