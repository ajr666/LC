class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        n = len(plants)

        i, j = 0, n - 1
        ans = 0
        A, B = capacityA, capacityB

        while i <= j: # 带等号，因为i == j时，也需消除(浇水)
            if i == j: # 意味着A, B要去处理同一个元素
                if max(A, B) < plants[i]:
                    ans += 1
            else:
                if A < plants[i]:
                    A = capacityA
                    ans += 1
                A -= plants[i]

                if B < plants[j]:
                    B = capacityB
                    ans += 1
                B -= plants[j]

            i += 1
            j -= 1

        return ans 