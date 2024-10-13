def solution(numbers):
    st = set()
    
    n = len(numbers)
    ans = 0
    
    for i in range(n):
        s = str(numbers[i])
        if s in st:
            ans += 1
        
        sl = list(s)
        a, b = 0, len(s) - 1
        while a < b:
            sl[a], sl[b] = sl[b], sl[a]
            ssw = ''.join(sl)
            if ssw in st:
                ans += 1
            a += 1
            b -= 1
                
        st.add(s)
        
    return ans
    
numbers = [1, 23, 156, 1650, 651, 165, 32]
numbers = [123, 321, 123]
print(solution(numbers))