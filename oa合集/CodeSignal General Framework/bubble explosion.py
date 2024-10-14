def solution(bubbles):
    m, n = len(bubbles), len(bubbles[0])
    
    exlpode = set()
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    for i in range(m):
        for j in range(n):
            ajcent = []
            
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < m and 0 <= y < n:
                    if bubbles[x][y] == bubbles[i][j]:
                        ajcent.append((x, y))
                        
            if len(ajcent) >= 2:
                exlpode.add((i, j))
                for aj in ajcent:
                    exlpode.add(aj)
                
    for i in range(m):
        for j in range(n):
            if (i, j) in exlpode:
                bubbles[i][j] = 0
                
    # print
    for i in range(m):
        print(bubbles[i])
    print("------")
                
    ans = [[0 for _ in range(n)] for _ in range(m)]
    
    for j in range(n):
        res = []
        for i in range(m - 1, -1, -1):
            if bubbles[i][j] != 0:
                res.append(bubbles[i][j])
        
        k = m - 1
        for r in res:
            ans[k][j] = r
            k -= 1
            
    
    # print
    for i in range(m):
        print(ans[i])
        

bubbles = [
  [3, 1, 2, 1],
  [1, 1, 1, 4],
  [3, 1, 2, 2],
  [3, 3, 3, 4]
]
solution(bubbles)