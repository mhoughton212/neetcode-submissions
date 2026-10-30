class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or 
                grid[row][col] == 0):
                return 0
            
            area = 1
            grid[row][col] = 0

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in dirs:
                area += dfs(row + dr, col + dc)

            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    res = max(res, area)

        return res