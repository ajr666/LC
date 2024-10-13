class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n

        def check(mid): # 检测是否有mid篇论文被引用了mid次
            if citations[-mid] >= mid:
                return True
            return False

        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1

        return l
            