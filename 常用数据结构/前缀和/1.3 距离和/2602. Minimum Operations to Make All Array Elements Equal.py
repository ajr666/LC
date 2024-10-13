import bisect


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        def biSearch(q): # 探寻 >= q 的区间左边界
            nonlocal n
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < q:
                    mid = l + 1
                else:
                    mid = r
    
        nums.sort()
        n = len(nums)

        preSum = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        ans = []

        print(preSum)

        for q in queries:
            j = biSearch(nums, q)
            print(j)
            left = q * j - preSum[j]
            right = preSum[n] - preSum[j] - (n - j) * q

            ans.append(left + right)

        return ans