class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        safe = set()

        def dfs(r, c):
            if (not (0 <= r < ROWS and 0 <= c < COLS) or
                (r, c) in safe or board[r][c] == "X"):
                return

            safe.add((r, c))
            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        for r in [0, ROWS - 1]:
            for c in range(COLS):
                if board[r][c] == "O":
                    dfs(r, c)

        for c in [0, COLS - 1]:
            for r in range(ROWS):
                if board[r][c] == "O":
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in safe:
                    board[r][c] = "X"
