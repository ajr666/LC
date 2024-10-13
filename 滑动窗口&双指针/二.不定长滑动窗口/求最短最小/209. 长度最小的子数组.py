class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        sum = 0
        ans = n + 1
        for r in range(n):
            sum += nums[r]

            while sum - nums[l] >= target:
                sum -= nums[l]
                l += 1

            if sum >= target:
                ans = min(ans, r - l + 1)

        if ans == n + 1:
            return 0
        return ans