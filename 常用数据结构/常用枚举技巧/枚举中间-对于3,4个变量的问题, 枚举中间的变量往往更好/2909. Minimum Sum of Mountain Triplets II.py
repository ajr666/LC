from cmath import inf


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)

        leftMin = [inf for _ in range(n)] # leftMin[i] records the min value in nums[0: i]
        rightMin = [inf for _ in range(n)] # rightMin[i] records the min value in nums[i: n]

        for i in range(1, n):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])

        for i in range(n - 2, 0, -1):
            rightMin[i] = min(rightMin[i + 1], nums[i + 1])
        
        print(leftMin)
        print(rightMin)

        ans = inf

        for i in range(1, n - 1):
            if leftMin[i] < nums[i] and nums[i] > rightMin[i]:
                ans = min(ans, leftMin[i] + nums[i] + rightMin[i])

        if ans == inf:
            return -1
        return ans