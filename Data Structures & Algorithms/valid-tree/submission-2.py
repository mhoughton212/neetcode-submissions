class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        start, dummy = 0, -1

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def containsCycle(node, parent):
            if node in visited:
                return True

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if containsCycle(neighbor, node):
                    return True

            return False

        res = not containsCycle(start, dummy) and len(visited) == n

        return res
