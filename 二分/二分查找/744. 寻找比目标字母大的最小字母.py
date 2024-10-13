class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)

        while l < r:
            mid = (l + r) // 2

            if ord(letters[mid]) < ord(target) + 1:
                l = mid + 1
            else:
                r = mid
        
        if l == len(letters):
            return letters[0]

        return letters[l]
