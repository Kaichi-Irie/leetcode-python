#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc code=start

from collections import defaultdict

CANNOT_DETERMINED = -1.0


class VariableGraph:
    """
    """

    def __init__(self):
        self._graph: dict[str, list[str]] = defaultdict(list)
        self.variable_names: set[str] = set()
        self.ratios: dict[tuple[str, str], float] = {}

    def contains(self, variable: str) -> bool:
        return variable in self.variable_names

    def dfs(self, start: str, destination: str, visited: set[str]) -> float:
        visited.add(start)
        if start == destination:
            return 1.0

        for neighbor in self._graph[start]:
            if neighbor in visited:
                continue
            val = self.dfs(neighbor, destination, visited)
            if val != CANNOT_DETERMINED:
                ratio = self.ratios[(start, neighbor)]
                return ratio * val
        return CANNOT_DETERMINED

    def add_variable_relation(self, var1: str, var2: str, ratio_of_var1_to_var2: float) -> None:
        self.variable_names.add(var1)
        self.variable_names.add(var2)

        # add variables
        self._graph[var1].append(var2)
        self._graph[var2].append(var1)

        # add ratios
        self.ratios[(var1, var2)] = ratio_of_var1_to_var2
        self.ratios[(var2, var1)] = 1 / ratio_of_var1_to_var2


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:

        graph = VariableGraph()
        for equation, ratio_of_a_to_b in zip(equations, values):
            a, b = equation
            graph.add_variable_relation(a, b, ratio_of_a_to_b)

        answers: list[float] = []
        for c, d in queries:
            if not graph.contains(c) or not graph.contains(d):
                answers.append(CANNOT_DETERMINED)
                continue
            answer = graph.dfs(c, d, set())
            answers.append(answer)
        return answers


# @lc code=end
