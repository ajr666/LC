class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stk = []
        ans = []
        set_ = set(target)

        idx = 0

        for num in range(1, n + 1):
            if num not in set_:
                ans.append('Push')
                ans.append('Pop')
            else:
                ans.append('Push')
                idx += 1

            if idx == len(target):
                return ans
            
        return ans