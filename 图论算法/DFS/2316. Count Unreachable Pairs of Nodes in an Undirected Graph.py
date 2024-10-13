class Solution:
    def dfs(self, u, graph, vis):
        cnt = 1
        for v in graph[u]:
            if v not in vis:
                vis.add(v)
                cnt += self.dfs(v, graph, vis)

        return cnt

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        vis = set()

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        ans = n * (n - 1) // 2

        for i in range(n):
            if i not in vis:
                vis.add(i)
                cnt = self.dfs(i, graph, vis)
                ans -= cnt * (cnt - 1) // 2

        return ans