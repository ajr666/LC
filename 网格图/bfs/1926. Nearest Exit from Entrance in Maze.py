from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        ei = entrance[0]
        ej = entrance[1]

        m = len(maze)
        n = len(maze[0])

        vis = [[False for _ in range(n)] for _ in range(m)]

        vis[ei][ej] = True
        q.append([ei, ej, 0])

        while q:
            v = q.popleft()
            x, y, d = v[0], v[1], v[2]

            for i in range(4):
                xi = x + dx[i]
                yi = y + dy[i]

                if 0 <= xi < m and 0 <= yi < n and maze[xi][yi] == '.':
                    if ([xi, yi] != [ei, ej]) and (xi + 1 == m or xi - 1 == -1  or yi + 1 == n or yi - 1 == -1):
                        return d + 1

                if not vis[xi][yi]:
                    vis[xi][yi] = True
                    q.append([xi, yi, d + 1])
                
        return -1