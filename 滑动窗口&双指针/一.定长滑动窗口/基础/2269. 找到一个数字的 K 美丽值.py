class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        a = [int(digit) for digit in str(num)]

        ans = 0
        t = 0
        mod = 10 ** (k - 1)
        
        for i in range(len(a)):
            t = t * 10 + a[i]
            print(t)

            if i >= k - 1:
                if t != 0 and num % t == 0:
                    ans += 1
                
                t = t % mod
        
        return ans