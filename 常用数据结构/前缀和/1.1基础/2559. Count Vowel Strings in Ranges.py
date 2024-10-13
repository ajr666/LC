class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        nums = [0 for _ in range(n)]
        st = set(['a', 'e', 'i', 'o', 'u'])

        for i in range(n):
            w = words[i]
            if w[0] in st and w[-1] in st:
                nums[i] = 1

        s = [0 for _ in range(n + 1)] # prefix fum
        for i in range(1, n + 1):
            s[i] = s[i - 1] + nums[i - 1]

        ans = []
        for q in queries:
            l, r = q[0], q[1]
            ans.append(s[r + 1] - s[l])

        return ans