class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        curr_distance = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                    if not (new_r < 0 or new_r == ROWS or new_c < 0 or new_c == COLS or
                        grid[new_r][new_c] != INF):
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = curr_distance + 1

            curr_distance += 1
        
