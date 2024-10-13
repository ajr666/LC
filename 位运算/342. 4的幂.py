class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        zero = one = 0

        while n:
            k = n & 1
            
            if k == 1:
                one += 1
            if k == 0:
                zero += 1
        
            if one > 1:
                return False

            n = n >> 1

        if not(one == 1 and zero % 2 == 0):
            return False
        
        return True