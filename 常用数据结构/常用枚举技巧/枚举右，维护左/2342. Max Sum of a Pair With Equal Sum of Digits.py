class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(n):
            s = 0
            while n:
                s += (n % 10)
                n = n // 10
            return s
        
        ans = -1
        
        d = dict() # digit sum, num

        for n in nums:
            s = digitSum(n)

            if s not in d:
                d[s] = n
            else:
                ans = max(ans, d[s] + n)
                d[s] = max(d[s], n)

        return ans