import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n, m = len(spells), len(potions)

        potions = sorted(potions)
        ans = []

        for spell in spells:
            tar = success / spell
            idx = bisect.bisect_left(potions, tar)

            ans.append(m - idx)

        return ans