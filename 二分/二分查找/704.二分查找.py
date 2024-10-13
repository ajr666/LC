class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        if l == len(nums) or nums[l] != target:
            return -1
        
        return l