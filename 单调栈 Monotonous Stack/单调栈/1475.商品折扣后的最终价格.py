class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [prices[i] for i in range(n)]
        st = []

        for i, p in enumerate(prices):
            if not st or prices[st[-1]] < p:
                st.append(i)
            else:
                while st and prices[st[-1]] >= p:
                    idx = st.pop()
                    ans[idx] = prices[idx] - p

                st.append(i)

        return ans