class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rows = set()
            for j in range(9):
                tile = board[i][j]
                if tile == ".":
                    continue
                if tile in rows:
                    return False
                rows.add(tile)

        for i in range(9):
            cols = set()
            for j in range(9):
                tile = board[j][i]
                if tile == ".":
                    continue
                if tile in cols:
                    return False
                cols.add(tile)
        
        for i in range(3):
            for j in range(3):
                squares = set()
                for k in range(3):
                    for l in range(3):
                        tile = board[k + 3 * i][l + 3 * j]
                        if tile == ".":
                            continue
                        if tile in squares:
                            return False
                        squares.add(tile)

        return True
