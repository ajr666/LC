class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        n = len(arr2)

        def searchLowerBound(tar):  # 返回 >= tar 区间的左边界
            l, r = 0, n

            while l < r:
                mid = (l + r) // 2
                if arr2[mid] < tar:
                    l = mid + 1
                else:
                    r = mid
            
            return l
        
        ans = 0
        
        for a1 in arr1:
            # lBound and rBound is the left and right element, which are coset to a1
            rBound = searchLowerBound(a1)
            lBound = rBound - 1 

            if (0 <= lBound < n and abs(arr2[lBound] - a1) <= d) or (0 <= rBound < n and abs(arr2[rBound] - a1) <= d):
                continue

            ans += 1

        return ans
