class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)

        diff = [0] * 1001
        
        for num, from_, to in enumerate(trips):
            diff[from_] += num
            diff[to + 1] -= num

        s = 0
        for i in range(1001):
            s += diff[i]
            if s > capacity:
                return False
        
        return True

        