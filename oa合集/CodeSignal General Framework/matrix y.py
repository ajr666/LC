def solution(matrix):
    n = len(matrix)
    
    def cal(a, b):
        nonlocal n
        res = 0
        
        y_st = set()
        
        for i in range((n - 1) // 2):
            if matrix[i][i] != a:
                res += 1
            if matrix[i][n - 1 - i] != a:
                res += 1
            y_st.add((i, i))
            y_st.add((i, n - 1 - i))
                
        for i in range((n - 1) // 2, n):
            if matrix[i][n // 2] != a:
                res += 1
            y_st.add((i, n // 2))
            
        for i in range(n):
            for j in range(n):
                if (i, j) not in y_st:
                    if matrix[i][j] != b:
                        res += 1
                        
        return res
    
    ans = n * n + 1
    for a in [0, 1, 2]:
        for b in [0, 1, 2]:
            if a != b:
                ans = min(cal(a, b), ans)
                
    return ans
    

matrix = [
    [2, 0, 0, 0, 2],
    [1, 2, 1, 2, 0],
    [0, 1, 2, 1, 0],
    [0, 0, 2, 1, 1],
    [1, 1, 2, 1, 1]
]
print(solution(matrix))