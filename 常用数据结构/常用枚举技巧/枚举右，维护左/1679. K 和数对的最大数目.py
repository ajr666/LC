class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = dict()
        n = len(nums)

        ans = 0

        for i in range(n):
            num = nums[i]

            if (k - num) in cnt:
                cnt[k - num] -= 1
                ans += 1
                if cnt[k - num] == 0:
                    cnt.pop(k - num)
            else:
                if num not in cnt:
                    cnt[num] = 1
                else:
                    cnt[num] += 1
                
        return ans