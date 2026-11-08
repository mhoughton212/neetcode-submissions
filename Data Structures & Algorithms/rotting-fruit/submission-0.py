class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        res = 0
        fresh_fruit = 0

        for r in range(ROWS):
            for c in range(COLS):
                tile = grid[r][c]
                if tile == 1:
                    fresh_fruit += 1
                elif tile == 2:
                    q.append((r, c))

        while fresh_fruit and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    fresh_fruit -= 1
                    q.append((nr, nc))
            res += 1


        return res if not fresh_fruit else -1