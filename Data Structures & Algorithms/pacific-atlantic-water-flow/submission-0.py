class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atlantic, pacific = set(), set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(ocean):
            q = deque(ocean)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if (not (0 <= nr < ROWS and 0 <= nc < COLS) 
                            or (nr, nc) in ocean or heights[nr][nc] < heights[r][c]):
                            continue
                        ocean.add((nr, nc))
                        q.append((nr, nc))

        for c in range(COLS):
            pacific.add((0, c))
            atlantic.add((ROWS - 1, c))
        for r in range(ROWS):
            pacific.add((r, 0))
            atlantic.add((r, COLS - 1))

        bfs(atlantic)
        bfs(pacific)

        return list(list(tile) for tile in atlantic & pacific)