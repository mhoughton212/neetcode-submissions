class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:set() for i in range(n)}

        for src, des in edges:
            graph[src].add(des)
            graph[des].add(src)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return
            
            visited.add(node)

            for i in graph[node]:
                if i == prev:
                    continue
                dfs(i, node)
            return

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
            dfs(i, -1)

        return res