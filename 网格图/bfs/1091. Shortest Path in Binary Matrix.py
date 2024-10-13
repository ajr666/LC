from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()

        m, n = len(grid), len(grid[0])

        vis = [[False for _ in range(n)] for _ in range(m)]

        if grid[0][0] == 1:
            return -1
        
        dx = [1, 0, -1, 0, -1, -1, 1, 1]
        dy = [0, 1, 0, -1, 1, -1, 1, -1]

        vis[0][0] = False
        q.append([0, 0, 0]) # x, y, d

        while q:
            info = q.popleft()
            x, y, d = info[0], info[1], info[2]
            if [x, y] == [m - 1, n - 1]:
                return d
            
            for i in range(8):
                xi = x + dx[i]
                yi = y + dy[i]

                if 0 <= xi < m and 0 <= yi < n:
                    if not vis[xi][yi] and grid[xi][yi] == 0:
                        vis[xi][yi] = True
                        q.append([xi, yi, d + 1])

        return -1