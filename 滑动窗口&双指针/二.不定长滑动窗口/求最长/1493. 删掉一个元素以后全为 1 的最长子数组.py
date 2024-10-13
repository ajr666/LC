from collections import defaultdict

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #子数组中最多出现2次0

        n = len(nums)
        cnt = defaultdict(int)

        l = 0
        ans = 0
        for r in range(n):
            # 调整左，直到右可以进
            while l < r and cnt[0] >= 2:
                cnt[nums[l]] -= 1
                l += 1
            
            cnt[nums[r]] += 1

            ans = max(ans, cnt[1])

        if ans == n:
            return n - 1
        return ans