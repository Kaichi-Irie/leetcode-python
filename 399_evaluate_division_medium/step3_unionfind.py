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
        # self.variables = defaultdict
        self.parents: dict[str, str] = {}
        self.ratios_to_parent: dict[str, float] = {}

    def add(self, x: str) -> None:
        if x in self.parents:
            return
        self.parents[x] = x
        self.ratios_to_parent[x] = 1.0

    def find(self, x: str) -> tuple[str, float] | None:
        if x not in self.parents:
            return None
        parent = self.parents[x]
        ratio_to_parent = self.ratios_to_parent[x]
        if parent == x:
            return parent, ratio_to_parent
        root, ratio_of_parent_to_root = self.find(parent)  # type: ignore
        ratio_to_root = ratio_to_parent * ratio_of_parent_to_root
        return root, ratio_to_root

    def unite(self, x: str, y: str, ratio_x_to_y) -> None:
        if x not in self.parents or y not in self.parents:
            raise ValueError("given variable is not added.")
        x_root, ratio_x_to_root = self.find(x)
        y_root, ratio_y_to_root = self.find(y)

        self.parents[x_root] = y_root
        self.ratios_to_parent[x_root] = (
            1 / ratio_x_to_root * ratio_x_to_y * ratio_y_to_root
        )


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        dsu = DSU()
        for (x, y), ratio_x_to_y in zip(equations, values):
            dsu.add(x)
            dsu.add(y)
            dsu.unite(x, y, ratio_x_to_y)

        answers = []
        for x, y in queries:
            x_root_and_ratio = dsu.find(x)
            y_root_and_ratio = dsu.find(y)
            if x_root_and_ratio is None or y_root_and_ratio is None:
                answers.append(CANNOT_DETERMINED)
                continue
            x_root, ratio_x_to_root = x_root_and_ratio  # type: ignore
            y_root, ratio_y_to_root = y_root_and_ratio  # type: ignore
            if x_root != y_root:
                answers.append(CANNOT_DETERMINED)
                continue
            ratio_x_to_y = ratio_x_to_root / ratio_y_to_root
            answers.append(ratio_x_to_y)
        return answers


# @lc code=end
