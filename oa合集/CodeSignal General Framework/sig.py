def solution(rates, strategy, k):
    n = len(rates)
    
    # 前缀和数组
    pre_sum = [0] * (n + 1)
    change_sum = [0] * (n + 1)
    
    # 计算初始利润的前缀和
    for i in range(1, n + 1):
        pre_sum[i] = pre_sum[i - 1] + strategy[i - 1] * rates[i - 1]
    
    # 计算改变后利润的前缀和
    for i in range(1, n + 1):
        change_sum[i] = change_sum[i - 1] + rates[i - 1]
    
    # 初始化答案为不改变策略时的利润
    ans = pre_sum[n]
    
    # 遍历所有可能的区间
    for i in range(k, n + 1):
        ans = max(ans, pre_sum[n] + (change_sum[i] - change_sum[i - k // 2] - (pre_sum[i] - pre_sum[i - k])))
    
    return ans

# 示例测试
vec1 = [2, 4, 1, 5, 10, 6]
vec2 = [-1, 1, 0, 1, -1, 0]
print(solution(vec1, vec2, 4))  # 输出: 18







# def solution(rates, strategy, k):
#     n = len(rates)
#     preSum = [0] * (n + 1)

#     for i in range(1, n + 1):
#         preSum[i] = preSum[i - 1] + rates[i - 1] * strategy[i - 1]

#     print(preSum)

#     s = preSum[n]

#     for i in range(0, n - k + 1):
#         t = 0
#         # for j in range(i, i + k // 2): # 前一半，0
#         #     if strategy[j] == -1:
#         #         t -= rates[j]
#         #     if strategy[j] == 1:
#         #         t += rates[j]

#         for j in range(i + k // 2, i + k): # 后一半，1
#             t += rates[j]
            
#         t += preSum[i] - preSum[0]
#         t += preSum[n] - preSum[i + k]

#         s = max(s, t)

#     print(s)

# rates = [2, 4, 1, 5, 10, 6]
# strategy = [-1, 1, 0, 1, -1, 0]
# k = 4
# solution(rates, strategy, k)