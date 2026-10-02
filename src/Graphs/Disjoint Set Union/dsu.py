
class dsu():
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n


    def find(self, n):
        root = self.parents[n]
        if self.parents[root] != root:
            self.parents[n] = self.find(root)
            return self.parents[n]
        return root



    def union(self, n1, n2):
        rep1 = self.find(n1)
        rep2 = self.find(n2)

        if rep1 == rep2: # same representative so belong in same set
            return False

        if self.rank[rep1] < self.rank[rep2]:
            self.parents[rep1] = rep2
        elif self.rank[rep1] > self.rank[rep2]:
            self.parents[rep2] = rep1
        else:
            self.parents[rep2] = rep1
            self.rank[rep1] += 1

