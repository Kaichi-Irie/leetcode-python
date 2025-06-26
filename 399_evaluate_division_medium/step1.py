#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc code=start

from collections import defaultdict

CANNOT_DETERMINED = -1.0


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:

        graph: dict[str, list[tuple[str, float]]] = defaultdict(list)
        variable_names: set[str] = set()
        for equation, rate_of_a_to_b in zip(equations, values):
            a, b = equation
            rate_of_b_to_a = 1 / rate_of_a_to_b
            variable_names.add(a)
            variable_names.add(b)
            graph[a].append((b, rate_of_a_to_b))
            graph[b].append((a, rate_of_b_to_a))

        answers: list[float] = []
        for c, d in queries:
            if c not in variable_names or d not in variable_names:
                answers.append(CANNOT_DETERMINED)
                continue
            answer = self.dfs(c, d, graph, set())
            answers.append(answer)
        return answers

    def dfs(self, start: str, destination: str, graph, visited: set[str]) -> float:
        visited.add(start)
        if start == destination:
            return 1.0

        for neighbor, ratio in graph[start]:
            if neighbor in visited:
                continue
            val = self.dfs(neighbor, destination, graph, visited)
            if val != CANNOT_DETERMINED:
                return ratio * val
        return CANNOT_DETERMINED


# @lc code=end
