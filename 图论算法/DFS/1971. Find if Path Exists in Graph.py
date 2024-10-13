class Solution:
    def dfs(self, i, g, vis):
        for v in g[i]:
            if vis[v] == False:
                vis[v] = True
                self.dfs(v, g, vis)

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        vis = [False for _ in range(n)]

        vis[source] = True
        self.dfs(source, g, vis)

        return vis[destination]