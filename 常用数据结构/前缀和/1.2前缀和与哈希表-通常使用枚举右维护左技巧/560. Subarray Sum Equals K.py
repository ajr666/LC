from collections import defaultdict
# 为什么这题不适合用滑动窗口做？
# 滑动窗口需要满足单调性，当右端点元素进入窗口时，窗口元素和是不能减少的。
# 本题 nums 包含负数，当负数进入窗口时，窗口左端点反而要向左移动，导致算法复杂度不是线性的。

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0 for _ in range(n + 1)] # prefix sum

        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        
        ans = 0
        cnt = defaultdict(int)
        for s in prefixSum:
            if s - k in cnt:
                ans += cnt[s - k]
            cnt[s] += 1
        
        return ans