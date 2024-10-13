class Solution:
    def searchLowerBound(self, nums, target) -> int: # 探寻 >=tar 区间的左边界
        l = 0
        r = len(nums) 

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid 
        
        return l
    
    def searchLowerBound2(self, nums, target): # 闭区间写法，无需+1 -1，比较方便
        l, r = -1, len(nums) # 探寻(-1, n)中每个数与tar的大小关系

        while l + 1 < r: # 循环退出条件l + 1 == r, 此时(l, r)中没有数
            # 循环不变量：
            # left 的回答一定为「是」
            # right 的回答一定为「否」
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid # (mid, right)
            else:
                r = mid # (l, mid)
            
        return l + 1 



        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        left = self.searchLowerBound(nums, target)

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        right = self.searchLowerBound(nums, target + 1) - 1

        return [left, right]