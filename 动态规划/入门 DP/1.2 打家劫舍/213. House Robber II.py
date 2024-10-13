class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]

        f1 = [0 for _ in range(n - 1)] # 0 - n-1
        f1[0] = nums[0]

        for i in range(1, n - 1): # 1 - n-1
            f1[i] = max(f1[i - 1], f1[i - 2] + nums[i]) # 初始时会用f[-1] = 0


        f2 = [0 for _ in range(n)] # 1 - n
        for i in range(1, n):
            f2[i] = max(f2[i - 1], f2[i - 2] + nums[i]) # 初始时会用f[-1] = 0

        return max(f1[n - 2], f2[n - 1])
