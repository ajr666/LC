from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = defaultdict(int) # 不会引发key error, 默认值为0
        n = len(s)

        ans = 0
        l = 0
        for r in range(n):
            # 调整左，直到右可以进
            while l < r and cnt[s[r]] >= 2:
                cnt[s[l]] -= 1
                l += 1

            # 右进
            cnt[s[r]] += 1

            ans = max(ans, r - l + 1)

        return ans