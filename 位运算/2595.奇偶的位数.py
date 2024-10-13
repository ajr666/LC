class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = odd = 0

        i = 0

        while n > 0:
            if i % 2 == 0:
                even += (n & 1)
            else:
                odd += (n & 1)

            n = n >> 1
            i += 1

        return [even, odd]