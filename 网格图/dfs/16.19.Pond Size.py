class Solution:
    def dfs(self, land, vis, x, y) -> int:
        cnt = 1

        dx = [1, -1, 0, 0, -1, -1, 1, 1]
        dy = [0, 0, 1, -1, -1, 1, -1, 1]

        for i in range(8):
            xi = x + dx[i]
            yi = y + dy[i]

            if 0 <= xi and xi < self.m:
                if 0 <= yi and yi <self.n:
                    if not vis[xi][yi] and land[xi][yi] == 0:
                        vis[xi][yi] = True
                        cnt += self.dfs(land, vis, xi, yi)
        
        return cnt


    def pondSizes(self, land: List[List[int]]) -> List[int]:
        self.m = len(land)
        self.n = len(land[0])

        ans = []

        vis = [[False for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if not vis[i][j] and land[i][j] == 0:
                    vis[i][j] = True
                    cnt = self.dfs(land, vis, i, j)
                    ans.append(cnt)
        
        ans.sort()

        return ans