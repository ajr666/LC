def solution(binaryString, requests):
    n = len(binaryString)
    bsL = [0] * n

    for i in range(n):
        bsL[i] = (int(binaryString[i]) + 1) % 2
    
    rbsL = [0] * n
    for i in range(n):
        rbsL[i] = (bsL[i] + 1) % 2
        
    print(bsL)
    print(rbsL)
    
    ps = [[0 for _ in range(n + 1)] for _ in range(2)] # preSum
    
    for i in range(1, n + 1):
        ps[0][i] = ps[0][i - 1] + bsL[i - 1]
        ps[1][i] = ps[1][i - 1] + rbsL[i - 1]
        
    print(ps)
    
    ans = []
    idx = 0
    for rq in requests:
        if rq[0] == 'c':
            i = int(rq[6:])
            print(i)
            ans.append(ps[idx][i + 1])
            
        else:
            idx = (idx + 1) % 2
            
    return ans
    

bs = "1111010"
bs = "11111111000000111110000000"
requests = ["count:15", "count:12", "flip", "count:4", "flip", "count:2"]
print(solution(bs, requests))