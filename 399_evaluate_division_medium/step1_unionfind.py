#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc code=start
from collections import defaultdict


class UnionFind:
    def __init__(self):
        self._parent_and_ratio: dict[str, tuple[str, float]] = {}
        self.nodes: set[str] = set()

    def add_node(self, node: str) -> None:
        if node in self._parent_and_ratio:
            return
        self._parent_and_ratio[node] = (node, 1.0)
        self.nodes.add(node)

    def find(self, node: str) -> tuple[str, float] | None:
        if node not in self.nodes:
            return None
        parent, node_to_parent_ratio = self._parent_and_ratio[node]
        if parent == node:
            return node, 1.0
        root, parent_to_root_ratio = self.find(parent)  # type: ignore
        node_to_root_ratio = parent_to_root_ratio * node_to_parent_ratio
        # path compression
        self._parent_and_ratio[node] = root, node_to_root_ratio
        return root, node_to_root_ratio

    def unite(self, node1: str, node2: str, ratio12) -> None:
        """
        we want to connect root1 to root2;
        node2 -> root2 <- root1 <- node1

        ratio12 = node1/node2
        node1_to_root1_ratio = node1/root1
        node2_to_root2_ratio = node2/root2

        root1_to_root2_ratio
        = root1/root2
        = root1/node1 * node2/root2 * node1/node2
        = 1/node1_to_root1_ratio * node2_to_root2_ratio * ratio12
        """
        if node1 not in self.nodes or node2 not in self.nodes:
            return
        root1, node1_to_root1_ratio = self.find(node1)  # type: ignore
        root2, node2_to_root2_ratio = self.find(node2)  # type: ignore
        root1_to_root2_ratio = 1 / node1_to_root1_ratio * node2_to_root2_ratio * ratio12
        self._parent_and_ratio[root1] = (root2, root1_to_root2_ratio)


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:

        dsu = UnionFind()
        for (a, b), ratio_ab in zip(equations, values):
            dsu.add_node(a)
            dsu.add_node(b)
            dsu.unite(a, b, ratio_ab)

        answers: list[float] = []
        for c, d in queries:
            if c not in dsu.nodes or d not in dsu.nodes:
                answer = -1.0
                answers.append(answer)
                continue

            c_root, c_ratio = dsu.find(c)  # type: ignore
            d_root, d_ratio = dsu.find(d)  # type: ignore
            if c_root == d_root:
                answer = c_ratio / d_ratio
            else:
                answer = -1.0
            answers.append(answer)

        return answers


# @lc code=end
