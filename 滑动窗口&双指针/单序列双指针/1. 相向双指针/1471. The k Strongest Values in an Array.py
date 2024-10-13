class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)

        n = len(arr)
        m = arr[int((n - 1) / 2)]

        i, j = 0, n - 1
        ans = []

        while k:
            k -= 1
            a = abs(arr[i] - m)
            b = abs(arr[j] - m)

            if a > b:
                ans.append(arr[i])
                i += 1
            elif a <= b:
                ans.append(arr[j])
                j -= 1

        return ans

        