class Solution:
    def dfs(self, grid, vis, x, y) -> int:
        cnt = grid[x][y]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]

            if 0 <= xi and xi < self.m:
                if 0 <= yi and yi <self.n:
                    if not vis[xi][yi] and grid[xi][yi] > 0:
                        vis[xi][yi] = True
                        cnt += self.dfs(grid, vis, xi, yi)

        return cnt


    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        
        self.m = len(grid)
        self.n = len(grid[0])

        vis = [[False for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] > 0 and vis[i][j] == False:
                    vis[i][j] = True
                    cnt = self.dfs(grid, vis, i, j)
                    
                    ans = max(ans, cnt)

        return ans
