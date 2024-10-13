class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        res = []

        used = [False for _ in range(n)]

        def backtrack(lev):
            if lev == n:
                ans.append(res[:])
                return
            
            for i in range(n):
                if used[i] == False:
                    res.append(nums[i])
                    used[i] = True

                    backtrack(lev + 1)

                    used[i] = False
                    res.pop()

        backtrack(0)

        return ans