class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = dict() # val, cnt
        ans = 0

        for i in range(0, len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        for val, cnt in d.items():
            print(val, cnt)
            ans += (cnt * (cnt - 1))/2

        return int(ans)