class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        n = len(s)
        ans = 0

        l = 0
        for r in range(n):
            # 调整 l, 直到 r 可以进
            while l < r and s[r] in st:
                st.remove(s[l])
                l += 1

            # r 进
            st.add(s[r])

            # 更新答案
            ans = max(ans, r - l + 1)

        return ans