class Solution:
    def searchLowerBound(self, nums, target) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] >= target:
                l = mid + 1
            else:
                r = mid

        return l


    def maximumCount(self, nums: List[int]) -> int:
        neg = self.searchLowerBound(nums, 0)

        pos_start = self.searchLowerBound(nums, 1)
        pos = len(nums) - 1 - pos_start + 1

        return max(pos, neg)