"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(size, r, c):
            if size == 1:
                return Node(grid[r][c] == 1, True)

            '''
            [1,1,1,0] --> [1]     [1, Flase, [1], [0], [0], [1]]
            [1,1,0,1]
            [1,1,1,1]
            [1,1,1,1]
            '''
            
            size = size // 2
            tl = dfs(size, r, c)
            tr = dfs(size, r, c + size)
            bl = dfs(size, r + size, c)
            br = dfs(size, r + size, c + size)

            if (
                tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and
                tl.val == tr.val == bl.val == br.val
            ):
                return Node(tl.val, True)
            
            return Node(tl.val, False, tl, tr, bl, br)

        return dfs(len(grid), 0, 0)
