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
        """
        First, we create a graph, and create two nodes and an edge for given an equation [A,B], value v (=A/B) like shown below
        A - v -> B
        A <- 1/v - B

        To answer each query, we check if start and target node are connected using DFS and return their ratio if connected.
        """
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(start: str, target: str, visited: set[str]) -> float:
            if start not in graph or target not in graph:
                return CANNOT_DETERMINED

            visited.add(start)
            if start == target:
                return 1.0
            for neighbor, ratio in graph[start].items():
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                ratio_neighbor_to_d = dfs(neighbor, target, visited)
                if ratio_neighbor_to_d != CANNOT_DETERMINED:
                    return ratio * ratio_neighbor_to_d

            return CANNOT_DETERMINED

        answers = []
        for c, d in queries:
            visited = set()
            answers.append(dfs(c, d, visited))
        return answers


# @lc code=end
