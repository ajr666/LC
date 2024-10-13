class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        MOD = 1_000_000_007

        # Kane calculates the Maximum val of arr
        def kane(arr):
            n = len(arr)
            f = [0 for _ in range(n)]

            f[0] = arr[0]
            for i in range(1, n):
                f[i] = max(f[i - 1] + arr[i], arr[i])

            if max(f) <= 0:
                return 0
            return max(f)

        s = sum(arr)

        val = kane(arr)
        
        arr.extend(arr)
        double_val = kane(arr)

        if s <= 0:
            if k >= 2:
                return double_val % MOD
            else:
                return val % MOD
        
        # if s > 0
        if k >= 2:
            return (double_val + (k - 2) * s) % MOD 
        return val % MOD