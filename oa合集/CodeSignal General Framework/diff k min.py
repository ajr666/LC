from math import inf
import bisect
def solution(nums, k):
    i = 0
    j = k
    n = len(nums)
    
    t = -inf
    q = inf
    ans = inf
    can_sub = []
    
    while j < n:
        bisect.insort_left(can_sub, nums[i])
        print(can_sub)
        
        print(nums[j])
        
        idx = bisect.bisect_left(can_sub, nums[j])
        if 0 <= idx < len(can_sub):
            ans = min(ans, abs(can_sub[idx] - nums[j]))
        if 0 <= idx - 1 < len(can_sub):
            ans = min(ans, abs(can_sub[idx - 1] - nums[j]))

        i += 1
        j += 1
        
    print(ans)
    
nums = [1, 5, 4, 10, 9]
# nums = [3, 102, 5, 8, 9]
solution(nums, 3)