class Dsu:
    def __init__(self, n):
        self.pa = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.pa[x] = y
        self.size[y] += self.size[x]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = Dsu(26)

        for eq in equations:
            a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
            if eq[1] == '=':
                dsu.union(a, b)
        
        for eq in equations:
            a, b = ord(eq[0]) - ord('a'), ord(eq[3]) - ord('a')
            if eq[1] == '!':
                if dsu.find(a) == dsu.find(b):
                    return False
                
        return True