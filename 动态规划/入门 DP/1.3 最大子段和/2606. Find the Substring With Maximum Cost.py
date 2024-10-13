class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d = dict()
        for i in range(len(chars)):
            d[chars[i]] = vals[i]

        def getVal(alpha):
            nonlocal d
            if alpha in d:
                return d[alpha]
            return ord(alpha) - ord('a') + 1
        
        n = len(s)

        f = [0 for _ in range(n)]

        f[0] = getVal(s[0])

        for i in range(1, n):
            f[i] = max(f[i - 1] + getVal(s[i]), getVal(s[i]))

        print(f)

        return max(max(f), 0)