class DSU:
    def __init__(self):
        self.parents = {}
        self.ranks = {}
        self.num_disjoint_sets = 0

    def add(self, item):
        self.parents[item] = item
        self.ranks[item] = 0
        self.num_disjoint_sets += 1

    def find(self, item):
        if item == self.parents[item]:
            return item
        root = self.find(self.parents[item])
        # Path compression
        self.parents[item] = root
        return root

    def unite(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)
        if root1 == root2:
            return
        # Union by rank
        if self.ranks[root1] > self.ranks[root2]:
            self.parents[root2] = root1
        elif self.ranks[root2] > self.ranks[root1]:
            self.parents[root1] = root2
        else:
            self.parents[root2] = root1
            self.ranks[root1] += 1

        self.num_disjoint_sets -= 1



dsu = DSU()

for i in range(4):
    dsu.add(i)

assert dsu.num_disjoint_sets == 4
dsu.unite(0, 1)
assert dsu.num_disjoint_sets == 3
assert dsu.find(0) == dsu.find(1)

dsu.unite(2, 3)
assert dsu.num_disjoint_sets == 2
assert dsu.find(2) == dsu.find(3)

dsu.unite(0, 3)
assert dsu.num_disjoint_sets == 1
assert all(dsu.find(0)==dsu.find(i) for i in range(4))

dsu.unite(0, 2)
assert dsu.num_disjoint_sets == 1
