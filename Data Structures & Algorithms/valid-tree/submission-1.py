class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i:set() for i in range(n)}

        for src, des in edges:
            graph[src].add(des)
            graph[des].add(src)

        #{0:(1,2,3), 1:(4)}
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            #(0,1,4)

            for i in graph[node]:
                if i == prev:
                    continue
                if not dfs(i, node):
                    return False

            return True

        
        return dfs(0, -1) and len(visited) == n
        