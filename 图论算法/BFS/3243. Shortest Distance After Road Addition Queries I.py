from collections import deque

# 暴力BFS
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for i in range(n - 1):
            g[i].append(i + 1)

        vis = set()
        
        def bfs():
            q = deque()
            
            vis.add(0)
            q.append([0, 0])

            while q:
                info = q.popleft()
                v, d = info[0], info[1]

                if v == n - 1:
                    return d
                
                for u in g[v]:
                    if u not in vis:
                        vis.add(u)
                        q.append([u, d + 1])
        
            return -1

        ans = []
        for e in queries:
            vis.clear()

            g[e[0]].append(e[1])
            ans.append(bfs())

        return ans