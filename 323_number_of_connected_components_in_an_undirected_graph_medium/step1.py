class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = {node:[] for node in range(n)}
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        visited = set()

        def traverse(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                traverse(neighbor)
                
        num_components = 0
        for node in range(n):
            if node in visited:
                continue
            traverse(node)
            num_components += 1
        return num_components
