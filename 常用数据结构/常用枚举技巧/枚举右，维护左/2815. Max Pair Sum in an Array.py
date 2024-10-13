class Solution:
    def extract_max_digit(self, n) -> int:
        res = 0
        while n:
            res = max(res, n % 10)
            n = n // 10

        return res

    def maxSum(self, nums: List[int]) -> int:
        d = dict() # max digit, number
        ans = -1

        for i in range(len(nums)):
            digit = self.extract_max_digit(nums[i])
            if digit not in d:
                d[digit] = nums[i]
            else:
                ans = max(ans, d[digit] + nums[i])
                d[digit] = max(d[digit], nums[i])

        return ans