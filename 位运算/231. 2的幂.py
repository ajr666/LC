class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        cnt = 0

        while n:
            cnt += (n & 1)
            
            if cnt > 1:
                return False
            
            n = n >> 1

        return True

# 法二：移除n最低位的1
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return n & (n - 1) == 0