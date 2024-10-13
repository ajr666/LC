class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vow = 0

        for i, c in enumerate(s):
            if c in "aeiou":
                vow += 1
            
            if i >= k:
                if s[i - k] in "aeiou":
                    vow -= 1

            ans = max(ans, vow)
        
        return ans