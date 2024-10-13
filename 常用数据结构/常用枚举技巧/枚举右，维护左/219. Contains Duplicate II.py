class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict() # val, idx

        for i in range(0, len(nums)):
            if nums[i] in d:
                if i - d[nums[i]] <= k:
                    return True
            d[nums[i]] = i
            
        return False