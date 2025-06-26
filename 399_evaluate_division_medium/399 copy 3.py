#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc code=start
from collections import defaultdict

CANNOT_DETERMINED = -1.0


class DSU:
    def __init__(self):
        self.parents = defaultdict(str)
        self.ratio_to_parent = defaultdict(float)

    def add(self, x: str) -> None:
        if x in self.parents:
            return
        self.parents[x] = x
        self.ratio_to_parent[x] = 1.0

    def find(self, x: str) -> tuple[str, float] | None:
        if x not in self.parents:
            return None
        parent = self.parents[x]
        if parent == x:
            return x, 1.0
        parent_find = self.find(parent)
        if parent_find is None:
            return None
        root, ratio_parent_to_root = parent_find

        ratio_to_parent = self.ratio_to_parent[x]
        ratio_to_root = ratio_to_parent * ratio_parent_to_root

        # path compression
        self.parents[x] = root
        self.ratio_to_parent[x] = ratio_to_root
        return root, ratio_to_root

    def unite(self, x, y, ratio_x_to_y) -> None:
        x_find = self.find(x)
        y_find = self.find(y)
        if x_find is None or y_find is None:
            return
        x_root, ratio_x_to_root = x_find
        y_root, ratio_y_to_root = y_find
        if x_root == y_root:
            return

        self.parents[x_root] = y_root
        self.ratio_to_parent[x_root] = (
            1 / ratio_x_to_root * ratio_y_to_root * ratio_x_to_y
        )

    def find_ratio(self, x, y) -> float:
        x_find = self.find(x)
        y_find = self.find(y)
        if x_find is None or y_find is None:
            return CANNOT_DETERMINED

        x_root, ratio_x_to_root = x_find
        y_root, ratio_y_to_root = y_find
        if x_root == y_root:
            return ratio_x_to_root / ratio_y_to_root
        return CANNOT_DETERMINED


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:

        dsu = DSU()
        for (a, b), val in zip(equations, values):
            dsu.add(a)
            dsu.add(b)
            dsu.unite(a, b, val)
        answers = []
        for c, d in queries:
            answer = dsu.find_ratio(c, d)
            answers.append(answer)

        return answers


# @lc code=end
