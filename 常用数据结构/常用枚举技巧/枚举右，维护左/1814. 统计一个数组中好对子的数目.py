class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(a): # 120
            if a == 0:
                return 0
            s = str(a) # '120'
            s = s[:: -1] # '021'
            sl = list(s) # ['0', '2', '1']

            i = 0
            while sl[i] == '0':
                i += 1

            sl_no_pre_zero = sl[i:] # ['2', '1']

            res = ''.join(sl)
            return int(res)

        cnt = dict()
        n = len(nums)

        ans = 0

        for i in range(n):
            t = nums[i] - rev(nums[i])
            if t in cnt:
                ans += cnt[t]
                cnt[t] += 1
            else:
                cnt[t] = 1

        MOD = 1_000_000_000 + 7
        return ans % MOD