from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefixSum = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]

        cnt = defaultdict(int)
        ans = 0
        for s in prefixSum:
            if s - goal in cnt:
                ans += cnt[s - goal]
            cnt[s] += 1

        return ans