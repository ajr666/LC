from collections import defaultdict, deque


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q = deque()
        vis = set()

        vis.add(id)
        for u in friends[id]:
            vis.add(u)
            q.append([u, 1])

        cnt = defaultdict(int)

        while q and level:

            info = q.popleft()
            v, d = info[0], info[1]
            if d == level:
                for video in watchedVideos[v]:
                    cnt[video] += 1

            for u in friends[v]:
                if u not in vis:
                    vis.add(u)
                    q.append([u, d + 1])

        print(cnt)

        sorted_cnt = sorted(cnt.items(), key = lambda x: (x[1], x[0]))
        ans = [it[0] for it in sorted_cnt]

        return ans