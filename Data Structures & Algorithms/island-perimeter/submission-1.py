class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if (row, col) in visited:
                return 0
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                (row, col) in visited or
                grid[row][col] == 0):
                return 1

            visited.add((row, col))
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            res = 0
            for dx, dy in dirs:
                res += dfs(row + dx, col + dy)

            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    return dfs(i, j)
        return 0