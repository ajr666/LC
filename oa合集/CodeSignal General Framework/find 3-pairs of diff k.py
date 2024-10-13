def solution(queries, k):
    cnt = dict()
    
    ans = []
    
    for q in queries:
        num = int(q[1:])
        if q[0] == '+':
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
                
        elif q[0] == '-':
            cnt.pop(num)
                
        print(cnt)
        
        res = 0
        for it in cnt.items():
            a = it[0]
            a_cnt = it[1]
            
            if (a + k) in cnt and (a + k * 2) in cnt:
                res += a_cnt * cnt[a + k] * cnt[a + k * 2]
        ans.append(res)
                
    return ans
    

qs = ["+4", "+5", "+6", "+4", "+3", "-4", "+-1", "+-2", "+-3"]
print(solution(qs, 1))