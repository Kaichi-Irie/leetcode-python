class UnionFind:
    def __init__(self, size: int):
        # parent[x]: parent of element x
        self.parent: list[int] = list(range(size))
        self.rank: list[int] = [0] * size

    def unite(self, x, y) -> None:
        x_root = self.find(x)
        y_root = self.find(y)

        # connect x_root <- y_root
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[y_root] = x_root
            self.rank[y_root] += 1
        # connect x_root -> y_root
        else:
            self.parent[x_root] = y_root
            self.rank[x_root] += 1

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        root = self.find(self.parent[x])
        self.parent[x] = root  # path compression
        return root

    def same(self, x, y) -> bool:
        root1 = self.find(x)
        root2 = self.find(y)
        return root1 == root2
