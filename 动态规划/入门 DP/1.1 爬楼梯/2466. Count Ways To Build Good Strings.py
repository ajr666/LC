class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        
        f = [0 for _ in range(high + 1)]
        f[0] = 1

        for i in range(1, high + 1):
            if i >= zero:
                f[i] += f[i - zero]
            
            if i >= one:
                f[i] += f[i - one]        

        return sum(f[low:]) % MOD