def solution(operation):
    leftMax, rightMax = 0, 0
    ans = []
    for op in operation:
        if op[0] == 0:
            a, b = op[1], op[2]
            if a > b:
                a, b = b, a
            
            leftMax = max(leftMax, a)
            rightMax = max(rightMax, b)
        
        print(leftMax, rightMax)
        if op[0] == 1:
            c, d = op[1], op[2]
            print("cd", c, d)
            if c > d:
                c, d = d, c
                
            if leftMax <= c and rightMax <= d:
                ans.append(True)
            else:
                ans.append(False)
                
    return ans

ops = [[0, 1, 3], [0, 4, 2], [1, 3, 4], [1, 3, 2]]
print(solution(ops))