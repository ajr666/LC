from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        que = deque()
        for card in deck:
            que.append(card)

        while len(que) > 1:
            que.popleft()
            if que:
                card = que.popleft()
                que.append(card)

        return que[0]
        
