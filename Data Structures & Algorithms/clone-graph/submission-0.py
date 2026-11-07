"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = defaultdict(List)

        def dfs(curr):
            if curr in node_map:
                return node_map[curr]
            
            clone = Node(curr.val)
            node_map[curr] = clone
            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
            
        return dfs(node) if node else None