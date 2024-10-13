class Solution:
    def dfs(self, grid, x, y, vis) -> int:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        cnt = 1  # 初始面积为1，因为当前格子是陆地

        for i in range(4):
            xi = x + dx[i]
            yi = y + dy[i]

            if 0 <= xi < len(grid) and 0 <= yi < len(grid[0]):
                if not vis[xi][yi] and grid[xi][yi] == 1:
                    vis[xi][yi] = True
                    cnt += self.dfs(grid, xi, yi, vis)
        
        return cnt

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        vis = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not vis[i][j]:
                    vis[i][j] = True
                    cnt = self.dfs(grid, i, j, vis)
                    ans = max(ans, cnt)

        return ans