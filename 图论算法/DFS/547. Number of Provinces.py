class Solution:
    def dfs(self, i, vis, isConnected, n):
        for j in range(n):
            if j != i and isConnected[i][j] == 1 and vis[j] == False:
                vis[j] = True
                self.dfs(j, vis, isConnected, n)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt = 0
        n = len(isConnected)
        vis = [False for _ in range(n)]

        for i in range(n):
            if vis[i] == False:
                vis[i] = True
                self.dfs(i, vis, isConnected, n)
                cnt += 1

        return cnt