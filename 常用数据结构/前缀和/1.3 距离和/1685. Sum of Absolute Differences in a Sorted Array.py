class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preSum = [0 for _ in range(n + 1)]

        for i in range(n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        
        ans = []
        for i in range(n):
            left = i * n[i] - preSum[i]
            right = preSum[n] - preSum[i + 1] - (n - i) * n[i]

            ans. append(left + right)

        return ans 