class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        g = [[] for _ in range(n)]

        for i, (x, y, r) in enumerate(bombs) :
            for j, (x1, y1, _) in enumerate(bombs) :
                if i != j :
                    if math.sqrt((x - x1)**2 + (y - y1)**2) <= r :
                        g[i].append(j)

        def dfs(x, vis, cnt) -> int :
            vis[x] = True

            for y in g[x] :
                if not vis[y] :
                    cnt += dfs(y, vis, cnt)

            return cnt

        ans = 0
        
        for i in n :
            vis = [False] * n

            ans = max(ans, dfs(i, vis, 0))
        
        return ans


        

