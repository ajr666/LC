class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)

        ne_greater = dict() # {x : x的下一个更大元素}

        st = []

        for n in nums2:
            if not st or st[-1] >= n:
                st.append(n)
            else:
                while st and st[-1] < n:
                    k = st.pop()
                    ne_greater[k] = n
                st.append(n)

        ans = []
        for n in nums1:
            if n in ne_greater:
                ans.append(ne_greater[n])
            else:
                ans.append(-1)

        return ans

