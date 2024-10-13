from math import inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0 for _ in range(n)]

        f[0] = nums[0]

        for i in range(1, n):
            f[i] = max(f[i - 1] + nums[i], nums[i])

        return max(f)


# 前缀和做法
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    s = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        s[i] = s[i - 1] + nums[i - 1]

    min_presum = 0
    ans = -inf
    for i in range(1, n + 1):
            ans = max(s[i] - min_presum, ans)
            min_presum = min(min_presum, s[i])

    return ans