class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        g = [[] for _ in range(n)]
        for e in connections:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        def dfs(v):
            for u in g[v]:
                if u not in vis:
                    vis.add(u)
                    dfs(u)

        cnt = 0
        vis = set()
        for v in range(n):
            if v not in vis:
                cnt += 1
                vis.add(v)
                dfs(v)

        return cnt - 1