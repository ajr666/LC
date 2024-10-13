class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0 for _ in range(n)]

        st = []

        for i, t in enumerate(temperatures):
            if not st or temperatures[st[-1]] >= t:
                    st.append(i)
            else:
                while st and temperatures[st[-1]] < t:
                    idx = st.pop()
                    ans[idx] = i - idx

                st.append(i)

        return ans