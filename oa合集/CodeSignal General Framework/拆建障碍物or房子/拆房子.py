from math import inf

def solution(houses, queries):
    houses.append(-5)
    houses.append(inf)
    
    m, n = len(houses), len(queries)
    
    houses = sorted(houses)
    seg = 0
    
    for i in range(1, m - 1):
        if houses[i] != houses[i - 1] + 1:
            seg += 1
    
    print("seg ", seg)
    
    h_st = set(houses)
    
    ans = []
    
    for q in queries:
        
        print(h_st)
        print(q)
        
        a = q - 1
        b = q + 1
        
        if a in h_st and b in h_st:
            seg += 1
                
        elif a in h_st or b in h_st:
            pass
            
        else:
            seg -= 1
            
        h_st.remove(q)
            
        ans.append(seg)
        
    return ans
    
    
h = [1, 2, 3, 6, 7, 9]
que = [6, 3, 7, 2, 9, 1]

print(solution(h, que))