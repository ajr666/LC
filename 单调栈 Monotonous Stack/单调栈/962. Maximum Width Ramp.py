class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = [] # idx, dis
        # dis is the max distance from nums[idx] to its next bigger element

        for i, n in enumerate(nums):
            print(nums(st[-1][0]))
            if not st or nums[st[-1][0]] > n:
                st.append([i, 0])
            else:
                dis = 0
                while not st and nums[st[-1][0]] <= n:
                    idx = st[-1][0]
                    dis = i - idx
                st.append([i, dis])

        print(st)