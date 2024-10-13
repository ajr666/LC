class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums.extend(nums) #使用append会导致循环引用
        ans = [-1 for _ in range(len(nums))]

        st = []

        for i, n in enumerate(nums):
            if not st or nums[st[-1]] >= n:
                st.append(i)
            else:
                while st and nums[st[-1]] < n:
                    idx = st.pop()
                    ans[idx] = n
                st.append(i)

        ans = ans[:len(nums) // 2]

        return ans