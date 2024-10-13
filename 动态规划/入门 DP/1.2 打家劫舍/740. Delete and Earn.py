class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0 for _ in range(n)]

        nums.sort()

        f[0] = nums[0]

        for i in range(1, n):
            j = i
            while j >= 0 and nums[j] == nums[i]:
                j -= 1
            
            k = j
            while k >= 0 and nums[k] == nums[i] - 1:
                k -= 1

            f[i] = max(f[k] + (i - j) * nums[i], f[j])

        return f[n - 1]