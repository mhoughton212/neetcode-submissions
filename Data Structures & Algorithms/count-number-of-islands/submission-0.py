class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(row, col):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                grid[row][col] == "0" or
                (row, col) in visited):
                return
            
            visited.add((row, col))

            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in dirs:
                dfs(row + dx, col + dy)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    res += 1

        return res