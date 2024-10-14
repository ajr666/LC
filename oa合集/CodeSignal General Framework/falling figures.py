def solution(matrix):
    m, n = len(matrix), len(matrix[0])
    
    obstacle = set()
    figs = []
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '#':
                obstacle.add((i, j))
            if matrix[i][j] == 'F':
                figs.append([i, j])
                matrix[i][j] = "-"
                
    print(figs)
                
    def can_fall():
        for _, f in enumerate(figs):
            x, y = f[0], f[1]
            x += 1
            if x > m:
                return False
            if matrix[x][y] == '#':
                return False
        
        return True
        
    while(can_fall()):
        for i in range(len(figs)):
            figs[i][0] += 1
    
    for x, y in figs:
        matrix[x][y] = 'F'
        
    for i in range(m):
        print(matrix[i])
        
    


matrix = [['F', 'F', 'F'],  
          ['-', 'F', '-'],  
          ['-', 'F', 'F'],  
          ['#', 'F', '-'],  
          ['F', 'F', '-'],
          ['-', '-', '-'],
          ['-', '-', '#'],  
          ['-', '-', '-']]

print(solution(matrix))           