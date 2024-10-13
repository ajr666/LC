class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        peri = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y):
            cnt = 4

            for i in range(4):
                xi = x + dx[i]
                yi = y + dy[i]
                if 0 <= xi < m and 0 <= yi < n and grid[xi][yi] == 1:
                    cnt -= 1

            peri += cnt

            for i in range(4):
                xi = x + dx[i]
                yi = y + dy[i]

                if 0 <= xi < m and 0 <= yi < n and grid[xi][yi] == 1:
                    if not vis[xi][yi]:
                        vis[xi][yi] = True
                        dfs(xi, yi)   

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)

        return peri           