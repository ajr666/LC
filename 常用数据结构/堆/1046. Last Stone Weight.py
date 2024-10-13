import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        res = -heap[0]

        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)

            res = abs(a - b)

            heapq.heappush(heap, -res)  

        return res
            