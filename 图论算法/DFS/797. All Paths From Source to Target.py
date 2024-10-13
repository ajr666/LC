class Solution:
    def dfs(self, u, graph, vis, path, res, n):
        if u == n - 1:
            res.append(path[:])
            return
        
        for v in graph[u]:
            if v not in vis:
                vis.add(v)
                path.append(v)
                self.dfs(v, graph, vis, path, res, n)
                vis.remove(v)
                path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        vis = set()

        n = len(graph)

        path = [0]
        vis.add(0)
        self.dfs(0, graph, vis, path, res, n)

        return res