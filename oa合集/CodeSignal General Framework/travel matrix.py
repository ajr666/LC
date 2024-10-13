def solution(matrix):
    n = len(matrix)
    weights = [] # first ele, w
    
    for i in range(n):
        x = i
        y = 0
        w = 0
        
        while 0 <= x < n and 0 <= y < n:
            w += matrix[x][y]
            x -= 1
            y += 1
            
        if x == -1:
            x += 1
            y -= 1
            w -= matrix[x][y]
        
        while 0 <= x < n and 0 <= y < n:
            w += matrix[x][y]
            x += 1
            y += 1
            
        weights.append([matrix[i][0], w])
        
    def sk(x):
        return (x[1], x[0])
        
    weights = sorted(weights, key=sk)
    print(weights)
    
    ans = []
    for i in range(n):
        ans.append(weights[i][0])
    
    return ans
    

mat = [[2, 3, 2],
       [0, 2, 5],
       [1, 0, 1]]
       
mat = [[1, 8, 4, 3, 4],
        [2, 8, 0, 3, 1],
        [0, 7, 9, 0, 8],
         [5, 0, 3, 1, 6],
         [1, 5, 0, 3, 1]]
print(solution(mat))