import heapq
import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        hp = []
        for g in gifts:
            heapq.heappush(hp, -g)

        s = -sum(hp)

        for _ in range(k):
            g = -heapq.heappop(hp)
            s -= g

            new_g = int(math.sqrt(g))
            heapq.heappush(hp, -new_g)
            s += new_g

        return s