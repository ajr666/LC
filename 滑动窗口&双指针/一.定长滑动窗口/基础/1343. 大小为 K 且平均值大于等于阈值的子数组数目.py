class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        wid_sum = sum(arr[:k])

        if wid_sum / k >= threshold:
            cnt += 1

        for i in range(k, len(arr)):
            wid_sum += arr[k]
            wid_sum -= arr[i - k]

            if wid_sum / k >= threshold:
                cnt += 1

        return cnt


            