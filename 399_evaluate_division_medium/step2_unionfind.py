#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc code=start
CANNOT_DETERMINED = -1.0


class UnionFind:
    def __init__(self):
        self._parent: dict[str, str] = {}
        self._ratio_to_parent: dict[str, float] = {}
        self._rank: dict[str, int] = {}

    def add_node(self, node: str) -> None:
        if node in self._parent:
            return
        self._parent[node] = node
        self._ratio_to_parent[node] = 1.0
        self._rank[node] = 0

    def find(self, node: str) -> tuple[str, float] | None:
        """
        find returns a pair for a given node; its parent and ratio of it to its parent.
        For better performance, we use path compression.
        """
        if node not in self._parent:
            return None
        parent = self._parent[node]
        node_to_parent_ratio = self._ratio_to_parent[node]
        if parent == node:
            return node, 1.0
        root, parent_to_root_ratio = self.find(parent)  # type: ignore
        # node/root = node/parent * parent/root
        node_to_root_ratio = node_to_parent_ratio * parent_to_root_ratio
        # path compression
        self._parent[node] = root
        self._ratio_to_parent[node] = node_to_root_ratio
        return root, node_to_root_ratio

    def unite(self, node1: str, node2: str, ratio_node1_to_node2) -> None:
        """
        we want to connect root1 to root2;
        node2 -> root2 <- root1 <- node1

        For better performance, we use union by rank

        ratio_node1_to_node2 = node1/node2
        node1_to_root1_ratio = node1/root1
        node2_to_root2_ratio = node2/root2
        """
        if node1 not in self._parent or node2 not in self._parent:
            return
        root1, node1_to_root1_ratio = self.find(node1)  # type: ignore
        root2, node2_to_root2_ratio = self.find(node2)  # type: ignore
        if root1 == root2:
            return

        # union by rank; swap node1 <-> node2 and root1 <-> root2
        if self._rank[root1] > self._rank[root2]:
            node1, node2 = node2, node1
            ratio_node1_to_node2 = 1 / ratio_node1_to_node2
            root1, root2 = root2, root1
            node1_to_root1_ratio, node2_to_root2_ratio = (
                node2_to_root2_ratio,
                node1_to_root1_ratio,
            )

        # root1_to_root2_ratio
        # = root1/root2
        # = root1/node1 * node2/root2 * node1/node2
        # = 1/node1_to_root1_ratio * node2_to_root2_ratio * ratio_node1_to_node2
        root1_to_root2_ratio = (
            (1 / node1_to_root1_ratio) * node2_to_root2_ratio * ratio_node1_to_node2
        )
        self._parent[root1] = root2
        self._ratio_to_parent[root1] = root1_to_root2_ratio
        if self._rank[root1] == self._rank[root2]:
            self._rank[root1] += 1


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
            c_root_and_ratio = dsu.find(c)
            d_root_and_ratio = dsu.find(d)
            # when variable c or d is not defined
            if not c_root_and_ratio or not d_root_and_ratio:
                answer = CANNOT_DETERMINED
                answers.append(answer)
                continue
            c_root, c_ratio = c_root_and_ratio
            d_root, d_ratio = d_root_and_ratio
            if c_root == d_root:
                answer = c_ratio / d_ratio
            else:
                answer = CANNOT_DETERMINED
            answers.append(answer)

        return answers


# @lc code=end
