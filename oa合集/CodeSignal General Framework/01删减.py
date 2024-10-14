from collections import deque
from math import inf

def solution(numbers, zereToOne):
    que = deque(numbers)
    
    num_zero = 0
    num_one = 0
    for i in range(len(numbers)):
        if numbers[i] == 0:
            num_zero += 1
        else:
            num_one += 1
    
    for i in range(1_000_000_000):
        print(que)
        if num_zero >= zereToOne:
            for _ in range(zereToOne):
                que.pop()
            que.appendleft(1)
            
            num_zero -= zereToOne
            num_one += 1
            
        elif num_one >= 1:
            k = 0
            while k < len(que) and que[k] == 1:
                k += 1
                
            k -= 1
            que[k] = 0
            num_zero += 1
            num_one -= 1
            
        else:
            break
            
    print(i)
    

numbers = [1, 1, 1, 0, 0, 0]
solution(numbers, 2)