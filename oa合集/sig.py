rates = [2, 4, 1, 5, 10, 6]
strategy = [-1, 1, 0, 1, -1, 0]
k = 4

# solution
n = len(rates)
preSum = [0] * (n + 1)

for i in range(1, n + 1):
    preSum[i] = preSum[i - 1] + rates[i - 1] * strategy[i - 1]

print(preSum)

s = preSum[n]

for i in range(0, n - k + 1):
    t = 0
    # for j in range(i, i + k // 2): # 前一半，0
    #     if strategy[j] == -1:
    #         t -= rates[j]
    #     if strategy[j] == 1:
    #         t += rates[j]

    for j in range(i + k // 2, i + k): # 后一半，1
        t += rates[j]
        
    t += preSum[i] - preSum[0]
    t += preSum[n] - preSum[i + k]

    s = max(s, t)

print(s)