from cmath import inf


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        l = 0

        sub = ""
        ans = ""
        minLen = inf

        for r in range(n):
            # pop left 1
            if s[r] == "1":
                while l < r and sub.count("1") >= k:
                    l += 1
                    sub = s[l: r]

            # continue to pop left 0
            while l < r and s[l] == "0":
                l += 1
            
            # push right
            sub = s[l: r + 1]

            # update ans
            if sub.count("1") == k:
                if len(sub) < minLen:
                    minLen = len(sub)
                    ans = sub
                elif len(sub) == minLen:
                    if sub < ans:
                        ans = sub
        
        return ans