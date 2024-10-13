class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # 分别求出子数组和的最大值, 和子数组和的最小值
        n = len(nums)

        if n == 1:
            return abs(nums[0])

        f1 = [0 for _ in range(n)]
        f1[0] = nums[0]

        for i in range(n):
            f1[i] = max(f1[i - 1] + nums[i], nums[i])

        f2 = [0 for _ in range(n)]
        f2[0] = nums[0]

        for i in range(n):
            f2[i] = min(f2[i - 1] + nums[i], nums[i])

        return max(max(f1), -min(f2))