class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)

        def check(divisor):
            # 计算每个 num 使用除数 divisor 的结果之和
            s = 0
            for num in nums:
                s += (num + divisor - 1) // divisor
            return s <= threshold

        # 二分查找最小的符合条件的除数
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid  # 尝试更小的除数
            else:
                left = mid + 1  # 尝试更大的除数

        return left