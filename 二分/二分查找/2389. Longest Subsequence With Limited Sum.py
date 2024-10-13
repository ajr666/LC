class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        preSum = [0] * (n + 1)

        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        ans = []

        print(preSum)

        for q in queries:
            idx = bisect.bisect_left(preSum, q + 1)
            ans.append(idx - 1)

        return ans
