class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)

        ans = n
        if '0' in num:
            ans = n - 1

        mp = {}

        for i in range(n - 1, -1, -1):
            if num[i] == '0':
                if '0' in mp:
                    ans = min(ans, n - i -2)
                mp['0'] = i
            
            elif num[i] == '5':
                if '0' in mp:
                    ans = min(ans, n - i - 2)
                mp['5'] = i
            
            elif num[i] == '2':
                if '5' in mp:
                    ans = min(ans, n - i - 2)
            
            elif num[i] == '7':
                if '5' in mp:
                    ans = min(ans, n - i - 2)

        return ans