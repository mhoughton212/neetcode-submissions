class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(i, row, col):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                (row, col) in visited or
                i >= len(word) or word[i] != board[row][col]):
                return False
            
            if i == len(word) - 1:
                return True
            
            visited.add((row, col))
            found = (dfs(i + 1, row - 1, col) or
                    dfs(i + 1, row + 1, col) or
                    dfs(i + 1, row, col - 1) or
                    dfs(i + 1, row, col + 1))
            visited.remove((row, col))

            return found
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(0, i, j):
                    return True
        return False