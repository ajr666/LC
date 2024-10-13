class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = wid_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            wid_sum += nums[i]
            wid_sum -= nums[i - k]

            max_sum = max(max_sum, wid_sum)

        return max_sum / k