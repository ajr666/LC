class Solution:
    def dfs(self, u, rooms, vis, n):
        for v in rooms[u]:
            if v not in vis:
                vis.add(v)
                self.dfs(v, rooms, vis, n)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis = set()
        n = len(rooms)

        vis.add(0)
        self.dfs(0, rooms, vis, n)

        return len(vis) == n