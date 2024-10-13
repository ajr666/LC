class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        d = dict() # val, idx

        for i in range(0, len(nums)):
            if target - nums[i] in d:
                ans.append(d[target - nums[i]])
                ans.append(i)
            d[nums[i]] = i

        return ans